import pytest

from manatee.api.exceptions import UnauthorizedException
from manatee.security.authorization import retrieve_token


def test_no_header():
    with pytest.raises(UnauthorizedException) as exception:
        retrieve_token(authorization="")

    assert "value_error.missing_auth_header" in str(exception.value)


def test_invalid_header_no_scheme():
    with pytest.raises(UnauthorizedException) as exception:
        retrieve_token(
            authorization="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ"
            "zdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOT"
            "I4MjMiLCJpYXQiOjE1Nzc4MzY4MDAuMCwiZXhwIjoxNTc3ODgwMDA"
            "wLjB9.ZhzV-LXNKx5od5q5kIFucu4qIppeOib21BKsb-ZuNts"
        )

    assert "value_error.invalid_scheme" in str(exception.value)


def test_invalid_header_wrong_scheme():
    with pytest.raises(UnauthorizedException) as exception:
        retrieve_token(authorization="Invalid ")

    assert "value_error.invalid_scheme" in str(exception.value)


def test_invalid_header_no_token():
    with pytest.raises(UnauthorizedException) as exception:
        retrieve_token(authorization="Bearer")

    assert "value_error.missing_token" in str(exception.value)


def test_valid_header():
    token = retrieve_token(
        authorization="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ"
        "zdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOT"
        "I4MjMiLCJpYXQiOjE1Nzc4MzY4MDAuMCwiZXhwIjoxNTc3ODgwMDA"
        "wLjB9.ZhzV-LXNKx5od5q5kIFucu4qIppeOib21BKsb-ZuNts"
    )
    assert (
        token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ"
        "zdWIiOiI3NjU5MDBlMS0wMjM5LTQ5OWEtOTlkNy02MTgzMTJmOT"
        "I4MjMiLCJpYXQiOjE1Nzc4MzY4MDAuMCwiZXhwIjoxNTc3ODgwMDA"
        "wLjB9.ZhzV-LXNKx5od5q5kIFucu4qIppeOib21BKsb-ZuNts"
    )
