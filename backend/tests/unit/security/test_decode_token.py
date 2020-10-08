from uuid import UUID

import pytest
from freezegun import freeze_time

from manatee.api.exceptions import UnauthorizedException
from manatee.security.authorization import decode_token


def test_empty_token():
    with pytest.raises(UnauthorizedException) as exception:
        decode_token("")

    assert "invalid_token" in str(exception.value)


def test_malformed_token():
    with pytest.raises(UnauthorizedException) as exception:
        decode_token("invalid")

    assert "invalid_token" in str(exception.value)


def test_expired_token():
    with pytest.raises(UnauthorizedException) as exception:
        decode_token(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjE1Nzc4MzY4MDAuMCwiZXhwIjoxNTc3ODgwMDAwLjB9.yT-rwDnSh4xG_QPlOV-uSv3K1R9zb-96sBwUm7OuuMI"  # noqa: E501
        )

    assert "expired_token" in str(exception.value)


@freeze_time("2020-01-01")
def test_token_with_invalid_uuid():
    with pytest.raises(UnauthorizedException) as exception:
        decode_token(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpbnZhbGlkIiwiaWF0IjoxNTc3ODM2ODAwLjAsImV4cCI6MTU3Nzg4MDAwMC4wfQ.a_nZ20jji_OKnxDY8O7lfQ3ZeDxMABdSAMNDKsNHv88"  # noqa: E501
        )

    assert "invalid_token" in str(exception.value)


@freeze_time("2020-01-01")
def test_valid_token():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjE1OTk1OTE0OTUuMzk4OTM3fQ.w1ekAfAJPCdgXMaOTMyPeGg6T8RHOR9TgBvvx0MlVS0"  # noqa: E501
    assert decode_token(token) == UUID("765900e1-0239-499a-99d7-618312f92823")
