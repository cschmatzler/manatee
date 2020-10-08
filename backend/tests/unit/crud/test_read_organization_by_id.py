import uuid
from uuid import UUID

from pony.orm.core import db_session

from manatee import database
from manatee.models.organization import DatabaseOrganization
from manatee.crud.organization import read_organization_by_id


def setup_module():
    database.setup()

    def insert_organizations():
        with db_session:
            DatabaseOrganization(
                id="a3b44076-4220-4e68-9388-112439ccb6f8",
                name="test_organization1",
                users=[],
            )
            DatabaseOrganization(
                id="765900e1-0239-499a-99d7-618312f92823",
                name="test_organization2",
                users=[],
            )

    insert_organizations()


def teardown_module(module):
    database.database.provider = database.database.schema = None


def test_read_invalid_organization():
    for i in range(0, 20):
        id = uuid.uuid4()
        assert not read_organization_by_id(id)


def test_read_existing_organization1():
    user = read_organization_by_id(UUID("a3b44076-4220-4e68-9388-112439ccb6f8"))
    assert user.name == "test_organization1"


def test_read_existing_organization2():
    user = read_organization_by_id(UUID("765900e1-0239-499a-99d7-618312f92823"))
    assert user.name == "test_organization2"
