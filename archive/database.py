import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from os import environ

DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
DATABASE_HOSTNAME = environ.get("DATABASE_HOSTNAME")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")

DATABASE_CONNECTION_STRING = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = _sql.create_engine(
    DATABASE_CONNECTION_STRING,
)

Session = _orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = _declarative._declarative_base()