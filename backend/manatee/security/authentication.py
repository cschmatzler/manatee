from __future__ import annotations  # TODO: Remove in Python 3.10

from passlib.hash import argon2  # type: ignore

from manatee.configuration import settings


class Password:
    """Argon 2 hash of a password"""

    hash: str

    def __init__(self, hash: str) -> None:
        """Initialize from a hashed password

        Parameters
        ----------
        hash : str
            Hashed password

        Returns
        -------
        PasswordHash

        Examples
        ------
        >>> password_hash = PasswordHash("$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA") # noqa: E501
        >>> password_hash.hash
        '$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA'
        """
        self.hash = hash

    def verify(self, plaintext: str) -> bool:
        """Verifies a password hash against a plain text string

        Parameters
        ----------
        plaintext : str
            The plain text string to verify

        Returns
        -------
        bool
            The result of verification

        Examples
        ------
        >>> password_hash = PasswordHash("$argon2id$v=19$m=256,t=2,p=8$IwRgbG0NwTgnBOD8n5OSMg$a8AJSE7H/ACMXQzFbXAJdA") # noqa: E501
        >>> password_hash.verify('password')
        True
        >>> password_hash.verify('invalid')
        False
        """
        return argon2.verify(plaintext, self.hash)

    @staticmethod
    def from_plaintext(plaintext: str) -> Password:
        """Creates a password hash from plain text string

        Parameters
        ----------
        plaintext : str
            The plain text password

        Returns
        -------
        PasswordHash

        Examples
        ------
        >>> password_hash = PasswordHash.from_plaintext("password") # doctest: +SKIP
        >>> password_hash.hash # doctest: +SKIP
        '$argon2id$v=19$m=256,t=2,p=8$ZG9jdGVzdHNhbHQ$wEpScpVu4o5QUgJHa/vLLg'
        """
        hash = argon2.using(
            type="ID",
            memory_cost=settings.ARGON2_MEMORY_COST,
            time_cost=settings.ARGON2_TIME_COST,
            parallelism=8,
        ).hash(plaintext)

        return Password(hash)
