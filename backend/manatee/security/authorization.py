import datetime
from uuid import UUID

from fastapi.params import Cookie
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

from manatee.api.exceptions import UnauthorizedException
from manatee.configuration import settings


def generate_token(sub: UUID) -> str:
    """Generates a JSON Web Token.

    Parameters
    ----------
    sub : str
        The token's subject ID

    Returns
    -------
    str
        The signed JSON Web Token

    Examples
    ------
    >>> generate_token(UUID("765900e1-0239-499a-99d7-618312f92823")) # doctest: +SKIP
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjE1Nzc4MzMyMDAuMCwiZXhwIjoxNTc3ODc2NDAwLjB9.2B7kWyCgF31I2nwIUXUfwhnNwigJJCi5qjsKm57-624'
    """

    iat: datetime.datetime = datetime.datetime.utcnow()
    # Set expiration of token to 12 hours
    exp: datetime.datetime = iat + datetime.timedelta(hours=12)

    token: str = jwt.encode(
        {"sub": f"{sub}", "iat": iat.timestamp(), "exp": exp.timestamp()},
        settings.JWT_SECRET,
        settings.JWT_ALGORITHM,
    )

    return token


def retrieve_token(authorization: str = Cookie("")) -> str:  # type: ignore
    """Retrieves a JSON Web Token from Authorization header

    Parameters
    ----------
    authorization : str
        The Authorization header, retrieved from FastAPI request

    Returns
    -------
    str
        The extracted JSON Web Token

    Raises
    ------
    UnauthorizedException
        If header is missing, invalid scheme or token is empty
    """
    if len(authorization) == 0:
        raise UnauthorizedException(
            "missing_auth_header", "missing authorization header"
        )

    scheme, _, param = authorization.partition(" ")

    if scheme.lower() != "bearer":
        raise UnauthorizedException("invalid_scheme", "invalid authorization scheme")
    elif len(param) == 0:
        raise UnauthorizedException(
            "missing_token", "token is missing from authorization header"
        )

    return param


def decode_token(token: str) -> UUID:
    """Decodes a JSON Web Token and returns the subject's UUID

    Parameters
    ----------
    token : str
        The JSON Web Token

    Returns
    -------
    UUID
        The subject's UUID

    Raises
    ------
    UnauthorizedException
        If token is invalid, contains invalid subject or is expired

    Examples
    ------
    >>> decode_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjE1OTk1OTE0OTUuMzk4OTM3fQ.w1ekAfAJPCdgXMaOTMyPeGg6T8RHOR9TgBvvx0MlVS0") # noqa: E501
    UUID('765900e1-0239-499a-99d7-618312f92823')
    """
    try:
        claims = jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        sub = UUID(claims["sub"])
    except ExpiredSignatureError:
        raise UnauthorizedException("expired_token", "token is expired")
    except (JWTError, ValueError):
        raise UnauthorizedException(
            "invalid_token", "token is not a valid json web token"
        )

    return sub
