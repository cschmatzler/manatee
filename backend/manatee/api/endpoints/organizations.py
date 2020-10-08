from fastapi.params import Depends
from fastapi.routing import APIRouter
from uuid import UUID

from manatee.security.authorization import decode_token, retrieve_token
from manatee.crud.user import (
    create_user as crud_create_user,
    read_user_by_id as crud_read_user_by_id,
    UserExistsError,
    OrganizationNotFoundError,
)
from manatee.crud.organization import create_organization as crud_create_organization
from manatee.models.user import UserCreate, UserResponse
from manatee.models.organization import OrganizationCreate, OrganizationResponse
from manatee.security.authentication import Password
from manatee.models.exception import Exception
from manatee.api.exceptions import ConflictException, NotFoundException

router = APIRouter()


@router.post("/", response_model=OrganizationResponse, status_code=201)
async def create_organization(body: OrganizationCreate):
    organization_id: UUID = crud_create_organization(body.name)

    return OrganizationResponse(id=organization_id, name=body.name)


@router.get("/{organization}/users/{user}")
async def read_user(
    organization: UUID, user: UUID, token: str = Depends(retrieve_token)
):
    uuid = decode_token(token)
    print(uuid)
    user = crud_read_user_by_id(uuid)
    print(user)
    return user


@router.post(
    "/{organization}/users",
    response_model=UserResponse,
    status_code=201,
    responses={409: {"model": Exception}},
)
async def create_user(organization: UUID, body: UserCreate):
    password = Password.from_plaintext(body.password)
    try:
        user_id: UUID = crud_create_user(organization, body.username, password)
    except OrganizationNotFoundError:
        raise NotFoundException("organization_not_found", "organization does not exist")
    except UserExistsError:
        raise ConflictException("user_exists", "user already exists")

    return UserResponse(id=user_id, username=body.username)
