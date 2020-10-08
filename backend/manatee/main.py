import uvicorn
from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from manatee import database
from manatee.api.router import router
from manatee.configuration import settings

# Create FastAPI app
app = FastAPI(
    title="Manatee",
    openapi_url="/api/openapi.json",
    # Make UJSON the default de-/serializer to impove speed
    default_response_class=UJSONResponse,
)
# Include all endpoints
app.include_router(router, prefix=settings.API_PREFIX)


def start():
    """Connect to the database and run the app through Uvicorn"""

    database.setup()
    uvicorn.run("manatee.main:app", host=settings.API_HOST, port=settings.API_PORT)
