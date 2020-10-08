from manatee.security.authentication import Password


def test_invalid_password():
    password = Password(
        "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"
    )
    assert not password.verify("invalid")


def test_valid_password():
    password = Password(
        "$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA"
    )
    assert password.verify("password")
