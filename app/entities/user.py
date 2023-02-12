from dataclasses import dataclass


@dataclass
class User:
    email: str = None
    first_name: str = None
    last_name: str = None
    password: str = None
    password_hash: str = None
    birth_date: int = None
    id: int = None
