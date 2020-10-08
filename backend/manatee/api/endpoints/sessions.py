from uuid import UUID

from fastapi import Response
from fastapi.routing import APIRouter

from manatee.api.exceptions import ForbiddenException
from manatee.models.exception import Exception
from manatee.models.session import SessionCreate
from manatee.security.authentication import Password
from manatee.security.authorization import generate_token
from manatee.crud.user import read_user_by_username as crud_read_user_by_username

router = APIRouter()


@router.post("/", responses={403: {"model": Exception}})
async def create_session(body: SessionCreate, response: Response):
    user = crud_read_user_by_username(body.organization, body.username)

    if not Password(user.password).verify(body.password):
        raise ForbiddenException("invalid_password", "password is invalid")

    token = generate_token(UUID(user["id"]))
    response.set_cookie(key="authorization", value=f"Bearer {token}")

    return user["username"]
