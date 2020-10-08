import random
import string
from uuid import UUID
import pytest

from pony.orm.core import db_session

from manatee import database
from manatee.crud.user import read_user_by_username, UserNotFoundError
from manatee.models.user import DatabaseUser
from manatee.models.organization import DatabaseOrganization


def setup_module():
    database.setup()

    def insert_organization():
        with db_session:
            DatabaseOrganization(
                id="08dfdc7a-511f-4ff5-8eb9-cff3730d0357", name="test_organization1"
            )

    def insert_users():
        with db_session:
            DatabaseUser(
                id="a3b44076-4220-4e68-9388-112439ccb6f8",
                organization=UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"),
                username="test_user1",
                password="$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA",  # noqa: E501
            )
            DatabaseUser(
                id="765900e1-0239-499a-99d7-618312f92823",
                organization=UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"),
                username="test_user2",
                password="$argon2id$v=19$m=256,t=2,p=8$HIOw1vpfixECAEBIaQ1BSA$YW51qRNn6Ap2fU5zzrbFEw",  # noqa: E501
            )

    insert_organization()
    insert_users()


def teardown_module():
    database.database.provider = database.database.schema = None


def test_read_invalid_user():
    for i in range(0, 20):
        username = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
        assert not read_user_by_username(
            UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"), username
        )


def test_read_existing_user_with_invalid_organization():
    assert not read_user_by_username(
        UUID("08dfdc7a-511f-4ff5-8eb9-000000000000"), "test_user1",
    )


def test_read_existing_user1():
    user = read_user_by_username(
        UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"), "test_user1"
    )
    assert user.id == UUID("a3b44076-4220-4e68-9388-112439ccb6f8")
    assert (
        user.password
        == "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"
    )


def test_read_existing_user2():
    user = read_user_by_username(
        UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"), "test_user2"
    )
    assert user.id == UUID("765900e1-0239-499a-99d7-618312f92823")
    assert (
        user.password
        == "$argon2id$v=19$m=256,t=2,p=8$HIOw1vpfixECAEBIaQ1BSA$YW51qRNn6Ap2fU5zzrbFEw"
    )
