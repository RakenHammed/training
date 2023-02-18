from sqlalchemy import Column, Integer, String

from app.database import Base


# pylint: disable=too-many-arguments
class SqlAlchemyUserRepository(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password_hash = Column(String(150), nullable=False)
    birth_date = Column(Integer, nullable=False)

    def __init__(
        self,
        email=None,
        first_name=None,
        last_name=None,
        password_hash=None,
        birth_date=None,
    ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = password_hash
        self.birth_date = birth_date

    def __repr__(self):
        return f"<User {self.id!r}>"
