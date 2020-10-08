import random
import re
import string

from manatee.security.authentication import Password


def test_hash_with_random_salt():
    for _ in range(0, 50):
        password = Password.from_plaintext(
            "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
        )
        regex = re.compile(r"\$argon2id\$v=\d{1,}\$m=\d{1,},t=\d{1,},p=8\$.{1,}\$.{1,}")

        assert regex.match(password.hash)
