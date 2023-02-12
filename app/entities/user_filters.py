from dataclasses import dataclass


@dataclass
class UserFilters:
    emails: list[str] = None
    birth_date: int = None
    ids: list[int] = None
