import os
from dataclasses import dataclass


@dataclass
class Config:
    my_api: str = os.environ.get("MY_API")
    database_uri: str = os.environ.get("DATABASE_URI")


config = Config()
