from uuid import UUID
from typing import Optional

from pony.orm.core import db_session

from manatee.models.user import DatabaseUser
from manatee.security.authentication import Password
from manatee.crud.organization import read_organization_by_id, OrganizationNotFoundError


class UserNotFoundError(BaseException):
    pass


class UserExistsError(BaseException):
    pass


def create_user(organization_id: UUID, username: str, password: Password) -> UUID:
    if not read_organization_by_id(organization_id):
        raise OrganizationNotFoundError()

    if read_user_by_username(organization_id, username):
        raise UserExistsError()
    else:
        with db_session:
            user = DatabaseUser(
                organization=organization_id, username=username, password=password.hash
            )

    return user.id


def read_user_by_id(organization_id: UUID, user_id: UUID) -> Optional[DatabaseUser]:
    with db_session:
        user = DatabaseUser.select(
            lambda user: user.organization.id == organization_id and user.id == user_id
        ).first()

    return user


def read_user_by_username(
    organization_id: UUID, username: str
) -> Optional[DatabaseUser]:
    with db_session:
        user = DatabaseUser.select(
            lambda user: user.organization.id == organization_id
            and user.username == username
        ).first()

    return user
