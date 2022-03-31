import os
from contextlib import contextmanager
from contextlib import AbstractContextManager

import psycopg2


@contextmanager
def connection() -> AbstractContextManager[None]:
    """Create and open up a connection to the application database."""
    db_connection = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_NAME"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host="db",
            port=5432,
        )

    try:
        yield db_connection

    finally:
        db_connection.close()


@contextmanager
def query() -> AbstractContextManager[None]:
    """Generate a database cursor to use for running queries."""
    with connection() as db:
        cursor = db.cursor()

        try:
            yield cursor

        finally:
            cursor.close()


def init() -> None:
    """Initialize the application database and prepare it for use."""
    with query() as db:
        db.execute(
            """
            create table topics (
                id          serial primary key,
                name        text   not null unique,
                description text
            );
            """
        )
