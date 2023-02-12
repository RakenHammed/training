from werkzeug.security import check_password_hash, generate_password_hash


class AuthentificationServices:
    def __init__(self):
        pass

    @staticmethod
    def generate_password_hash(password) -> str:
        if password:
            return generate_password_hash(password=password)
        raise Exception("Password can not be empty")

    @staticmethod
    def check_password_hash(password_hash, password) -> bool:
        return check_password_hash(pwhash=password_hash, password=password)
