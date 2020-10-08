from datetime import datetime
from uuid import UUID, uuid4

import pydantic
from pony.orm.core import Optional, PrimaryKey, Required

from manatee.database import database


class DatabaseUser(database.Entity):  # type: ignore
    """User ORM model"""

    id = PrimaryKey(UUID, default=uuid4)
    organization = Required("DatabaseOrganization")
    username = Required(str)
    password = Required(str)
    date_created = Required(datetime, default=datetime.utcnow)
    modified_at = Optional(datetime)


class UserResponse(pydantic.BaseModel):
    """Response model for users"""

    id: UUID
    username: str


class UserCreate(pydantic.BaseModel):
    """Create model for users"""

    username: str
    password: str
