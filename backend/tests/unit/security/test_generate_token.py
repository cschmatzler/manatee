import uuid
from uuid import UUID

from freezegun import freeze_time

from manatee.security.authorization import generate_token


def test_random_sub():
    for _ in range(0, 50):
        sub = uuid.uuid4()
        generate_token(sub)


@freeze_time("2000-01-01")
def test_correct_expiration_2000():
    sub = UUID("765900e1-0239-499a-99d7-618312f92823")
    token = generate_token(sub)
    assert (
        token
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjk0NjY4NDgwMC4wLCJleHAiOjk0NjcyODAwMC4wfQ.qyIUr8VtyXuqb9-gA_CRRzRND_ovTdSbehFt27pbrFk"  # noqa: E501
    )


@freeze_time("2020-01-01")
def test_correct_expiration_2020():
    sub = UUID("765900e1-0239-499a-99d7-618312f92823")
    token = generate_token(sub)
    assert (
        token
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOTI4MjMiLCJpYXQiOjE1Nzc4MzY4MDAuMCwiZXhwIjoxNTc3ODgwMDAwLjB9.yT-rwDnSh4xG_QPlOV-uSv3K1R9zb-96sBwUm7OuuMI"  # noqa: E501
    )
