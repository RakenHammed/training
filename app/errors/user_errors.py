class EmailNotFoundError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class PasswordDoesNotMatchError(Exception):
    pass


class UserIdDoesNotExists(Exception):
    pass
