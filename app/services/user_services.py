from typing import List

from app.entities.credentials import Credentials
from app.entities.user import User
from app.entities.user_filters import UserFilters
from app.errors.user_errors import (
    EmailAlreadyExistsError,
    EmailNotFoundError,
    PasswordDoesNotMatchError,
)
from app.repositories.user_repository import UserRepository
from app.services.authentification_services import AuthentificationServices


class UserServices:
    def __init__(self):
        self.__authentification_services = AuthentificationServices()
        self.__user_repository: UserRepository = UserRepository()

    def get_one_by(self, _id) -> User:
        return self.__user_repository.get_by(_id)

    def get_all_by(self, filters: UserFilters) -> List[User]:
        return self.__user_repository.get_all_by(filters)

    def create(self, user: User) -> User:
        self.raise_error_if_email_exists(user.email)
        user.password_hash = self.__authentification_services.generate_password_hash(
            user.password
        )
        return self.__user_repository.create(user)

    def update(self, _id, user: User) -> User:
        if user.password:
            user.password_hash = (
                self.__authentification_services.generate_password_hash(user.password)
            )
        return self.__user_repository.update(_id, user)

    def delete(self, _id) -> None:
        return self.__user_repository.delete(_id)

    def get_user_if_valid(self, credentials: Credentials) -> User:
        user = self.get_user_if_email_exists_else_error(credentials.email)
        self.check_if_valid_password_else_error(credentials.password, user)
        return user

    def get_user_if_email_exists_else_error(self, email: str) -> User:
        filters: UserFilters = UserFilters(emails=[email])
        users: list[User] = self.get_all_by(filters)
        if users:
            return users[0]
        raise EmailNotFoundError("Email not found")

    def check_if_valid_password_else_error(self, password: str, user: User) -> None:
        if not self.__authentification_services.check_password_hash(
            password_hash=user.password_hash, password=password
        ):
            raise PasswordDoesNotMatchError("Password does not match")

    def raise_error_if_email_exists(self, email: str) -> None:
        filters: UserFilters = UserFilters(emails=[email])
        users: list[User] = self.get_all_by(filters)
        if users:
            raise EmailAlreadyExistsError("Email already exists")
