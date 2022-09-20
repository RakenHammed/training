from logging.config import dictConfig


class LoggerSetup:
    def __init__(self):
        dictConfig(
            {
                'version': 1,
                'formatters': {
                    'default': {
                        'format': '[%(asctime)s] %(levelname)s : %(message)s',
                    }
                },
                'handlers': {
                    'wsgi': {
                        'class': 'logging.StreamHandler',
                        'stream': 'ext://flask.logging.wsgi_errors_stream',
                        'formatter': 'default'
                    },
                    "file": {
                        "level": "DEBUG",
                        "class": "logging.handlers.RotatingFileHandler",
                        "filename": "./logs/main.log",
                        "delay": True,
                        "formatter": "default",
                    },
                },
                'root': {
                    'level': 'DEBUG',
                    'handlers': ['wsgi', 'file']
                }
            }
        )
