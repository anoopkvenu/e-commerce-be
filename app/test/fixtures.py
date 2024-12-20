import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy_utils import create_database, drop_database, database_exists
from config import Settings

from database import Base

from test.utils import TestDatabase


fixture_used = False

@pytest.fixture(scope="session", autouse=True)
def create_and_delete_database():
    global fixture_used

    if fixture_used:
        yield
        return

    if database_exists(Settings.TEST_DATABASE_URL):
        drop_database(Settings.TEST_DATABASE_URL)

    create_database(Settings.TEST_DATABASE_URL)

    test_engine = create_engine(Settings.TEST_DATABASE_URL)

    Base.metadata.create_all(bind=test_engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

    TestDatabase(session=SessionLocal()).populate_test_database()
    fixture_used = True
    yield

    close_all_sessions()

    drop_database(Settings.TEST_DATABASE_URL)