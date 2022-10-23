import dataclasses
import os


@dataclasses
class Config:
    MY_API = os.environ.get("MY_API")
    DATABASE_URI = os.environ.get("DATABASE_URI")
