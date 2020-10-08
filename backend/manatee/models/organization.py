from datetime import datetime
from uuid import UUID, uuid4
import pydantic

from pony.orm.core import Optional, PrimaryKey, Required, Set

from manatee.database import database


class DatabaseOrganization(database.Entity):  # type: ignore
    """Organization ORM model"""

    id = PrimaryKey(UUID, default=uuid4)
    name = Required(str)
    users = Set("DatabaseUser")
    date_created = Required(datetime, default=datetime.utcnow)
    modified_at = Optional(datetime)


class OrganizationResponse(pydantic.BaseModel):
    """Response model for organizations"""

    id: UUID
    name: str


class OrganizationCreate(pydantic.BaseModel):
    """Create model for organizations"""

    name: str
