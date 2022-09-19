import os


class Config(object):
    MY_API = os.environ.get("MY_API")
    ENV = os.environ.get("ENV")
