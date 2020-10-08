from uuid import UUID
from typing import Optional

from pony.orm.core import db_session

from manatee.models.organization import DatabaseOrganization


class OrganizationNotFoundError(BaseException):
    pass


def create_organization(name: str) -> UUID:
    with db_session:
        organization = DatabaseOrganization(name=name)

    return organization.id


def read_organization_by_id(organization_id: UUID) -> Optional[DatabaseOrganization]:
    with db_session:
        organization = DatabaseOrganization.select(
            lambda organization: organization.id == organization_id
        ).first()

    return organization
