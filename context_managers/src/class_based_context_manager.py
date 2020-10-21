"""This code is just to demonstrate the usage of a context manager. The actual usage of the SqlAlchemy library involves setting up a connection to the database engine and a table. 

If you wish to learn to use the SqlAlchemy library to work with databases, I recommend following the tutorials at the links listed below:

https://youtu.be/xMT3ckHOrx0 (Python 101 by Mike Driscoll)
https://realpython.com/python-sqlite-sqlalchemy/ (Real Python)"""


from sqlalchemy.orm import Session


class DBConnect:
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.session.commit()
        else:
            # Use logging instead of print statements in production code.
            print(f"Exception: {exc_type}")
            print(f"Traceback: {traceback}")
            self.session.rollback()


with DBConnect() as connector:
    # Perform database operation.
    pass
