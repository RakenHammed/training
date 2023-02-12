from typing import List

from sqlalchemy.exc import DatabaseError

from app import database
from app.entities.user import User
from app.entities.user_filters import UserFilters
from app.errors.sql_database_errors import SqlDatabaseError
from app.errors.user_errors import UserIdDoesNotExists
from app.repositories.entity_repository import EntityRepository
from app.repositories.sql_alechemy_user_repository import SqlAlechemyUserRepository
from app.repositories.user_sql_alchemy_filters_builder import (
    UserSqlAlchemyFiltersBuilder,
)


class UserRepository(EntityRepository):
    def __init__(self):
        self.__database = database
        self.__sql_alechemy_user_repository = SqlAlechemyUserRepository
        self.__user_sql_alchemy_filters_builder = UserSqlAlchemyFiltersBuilder(
            self.__sql_alechemy_user_repository
        )

    def get_by(self, _id=None) -> User:
        try:
            user = self.__sql_alechemy_user_repository.query.get(_id)
            return self._to_entity_from(user, User())
        except DatabaseError as error:
            raise SqlDatabaseError("Something went wrong") from error

    def get_all_by(self, filters: UserFilters) -> List[User]:
        try:
            users = self.__sql_alechemy_user_repository.query.filter(
                *self.__user_sql_alchemy_filters_builder.build_from(filters)
            ).all()
            return self._to_entities_from(users, User())
        except DatabaseError as error:
            raise SqlDatabaseError("Something went wrong") from error

    def create(self, entity: User) -> User:
        try:
            user_orm = self.__sql_alechemy_user_repository(
                email=entity.email,
                first_name=entity.first_name,
                last_name=entity.last_name,
                password_hash=entity.password_hash,
                birth_date=entity.birth_date,
            )
            self.__database.session.add(user_orm)
            self.__database.session.commit()
            return self._to_entity_from(user_orm, User())
        except DatabaseError as error:
            raise SqlDatabaseError("Something went wrong") from error

    def update(self, _id, entity: User) -> User:
        try:
            user_orm = self.__sql_alechemy_user_repository.query.get(_id)
            if not user_orm:
                raise UserIdDoesNotExists("User not found")
            if entity.email:
                user_orm.email = entity.email
            if entity.first_name:
                user_orm.first_name = entity.first_name
            if entity.last_name:
                user_orm.last_name = entity.last_name
            if entity.password_hash:
                user_orm.password_hash = entity.password_hash
            if entity.birth_date:
                user_orm.birth_date = entity.birth_date
            self.__database.session.commit()
            return self._to_entity_from(user_orm, User())
        except DatabaseError as error:
            raise SqlDatabaseError("Something went wrong") from error

    def delete(self, _id) -> None:
        user = self.get_by(_id=_id)
        if not user:
            raise UserIdDoesNotExists("User not found")
        try:
            self.__database.session.delete(user)
            self.__database.session.commit()
        except DatabaseError as error:
            raise SqlDatabaseError("Something went wrong") from error
