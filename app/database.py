from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from app.config import config

engine = create_engine(url=config.database_uri)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base(
    metadata=MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
)
Base.query = session.query_property()


def init_db(app):
    app.teardown_appcontext(close_db)
    Base.metadata.create_all(bind=engine)


def close_db(exception=None):
    session.remove()
