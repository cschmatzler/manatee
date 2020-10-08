from uuid import UUID
import pydantic


class SessionCreate(pydantic.BaseModel):
    """Create model for sessions"""

    organization: UUID
    username: str
    password: str
