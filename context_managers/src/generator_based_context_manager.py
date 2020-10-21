"""This code is just to demonstrate the usage of a context manager. The actual usage of the SqlAlchemy library involves setting up a connection to the database engine and a table. 

If you wish to learn to use the SqlAlchemy library to work with databases, I recommend following the tutorials at the links listed below:

https://youtu.be/xMT3ckHOrx0 (Python 101 by Mike Driscoll)
https://realpython.com/python-sqlite-sqlalchemy/ (Real Python)"""

from contextlib import contextmanager

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


@contextmanager
def db_connect():
    session = Session()
    try:
        yield session
    except SQLAlchemyError as error:
        # Use logging instead of print statements in production code.
        print(f"{error.__class__.__name__}: {error}")
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()


with db_connect() as connector:
    # Perform database operation.
    pass
