from pony import orm

from manatee.configuration import settings

database = orm.Database()


def setup():
    """Connect to the database.

    In case of a file database, create the file and generate entity mappings as well.
    """
    if settings.DATABASE_PROVIDER == "sqlite":
        database.bind(
            provider="sqlite", filename=settings.DATABASE_FILENAME, create_db=True
        )
        database.generate_mapping(create_tables=True)
    elif settings.DATABASE_PROVIDER == "postgres":
        database.bind(
            provider="postgres",
            host=settings.DATABASE_SOCKET,
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            database=settings.DATABASE_NAME,
        )
