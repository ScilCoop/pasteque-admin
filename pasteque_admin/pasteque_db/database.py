# This file contains the Database class

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL as SqlaURL

class Credentials:
    """ This class holds user-specific database credentials """

    def __init__(self, **kwargs):
        """ Kwargs can contains credentials """
        self.host = None
        self.port = None
        self.user = None
        self.password = None
        self.name = None
        self.driver = None # e.g mysql, postgresql, ...

        self.configure(**kwargs)

    def configure(self, **kwargs):
        """ Set credentials by looking kargs """
        for field in ('host', 'port', 'user', 'password', 'driver', 'name'):
            if field in kwargs:
                setattr(self, field, kwargs[field])

    def generate_sqla_url(self):
        """ Return a sqlalchemy.engine.url.URL """
        return SqlaURL(
            self.driver,
            self.user,
            self.password,
            self.host,
            self.port,
            self.name,
        )

    def __repr__(self):
        return "%s://%s:%s@%s:%s/%s" % (self.driver, self.user,
            self.password, self.host, self.port, self.name)

class Database:
    """ Hold SQLAlchemy objects (engine and session class).
    Handle some procedures like database connection and session making.
    """

    def __init__(self, sqla_url=None):
        self.engine = None
        self.SessionClass = None
        self.sqla_url = None

        if sqla_url is not None:
            self.setup(sqla_url)

    def setup(self, sqla_url):
        """ Take a sqlalchemy.engine.url.URL and setup the engine,
        create the session class """
        self.sqla_url = sqla_url
        self.engine = create_engine(sqla_url)
        self.SessionClass = sessionmaker(bind=self.engine)

    def new_session(self):
        if self.engine is None or self.SessionClass is None:
            raise RuntimeError("Pasteque database used before being configured")
        else:
            return self.SessionClass()

    def __repr__(self):
        return "e: %s - s: %s" % (self.engine, self.SessionClass)
