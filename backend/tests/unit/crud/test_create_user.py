from uuid import UUID

import pytest
from pony.orm.core import db_session

from manatee import database
from manatee.crud.user import UserExistsError, create_user
from manatee.models.organization import DatabaseOrganization
from manatee.crud.organization import OrganizationNotFoundError
from manatee.models.user import DatabaseUser
from manatee.security.authentication import Password


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
                organization=UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"),
                id="a3b44076-4220-4e68-9388-112439ccb6f8",
                username="test_user1",
                password="$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA",  # noqa: E501
            )

    insert_organization()
    insert_users()


def teardown_module():
    database.database.provider = database.database.schema = None


def test_create_user_already_exists(mocker):
    mocker.patch("manatee.crud.organization.read_organization_by_id", return_value=None)
    mocker.patch("manatee.crud.user.read_user_by_username", return_value="not-none")

    with pytest.raises(UserExistsError):
        create_user(
            UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"),
            "test_user1",
            Password(
                "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"  # noqa: E501
            ),
        )


def test_create_user_with_invalid_organization(mocker):
    mocker.patch("manatee.crud.organization.read_organization_by_id", return_value=None)

    with pytest.raises(OrganizationNotFoundError):
        create_user(
            UUID("08dfdc7a-511f-4ff5-8eb9-000000000000"),
            "test_user2",
            Password(
                "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"  # noqa: E501
            ),
        )


def test_create_user(mocker):
    mocker.patch(
        "manatee.crud.organization.read_organization_by_id", return_value="not-none"
    )
    mocker.patch("manatee.crud.user.read_user_by_username", return_value=None)

    user_id = create_user(
        UUID("08dfdc7a-511f-4ff5-8eb9-cff3730d0357"),
        "test_user2",
        Password(
            "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"  # noqa: E501
        ),
    )

    assert isinstance(user_id, UUID)
