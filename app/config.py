import os
from dataclasses import dataclass


@dataclass
class Config:
    testing: bool = bool(os.environ.get("TESTING", ""))
    my_api: str = os.environ.get("MY_API")
    database_uri: str = (
        os.environ.get("DATABASE_URI_TEST")
        if bool(os.environ.get("TESTING", ""))
        else os.environ.get("DATABASE_URI")
    )
