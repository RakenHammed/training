FROM python:3.10-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.1


RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /application
COPY ../poetry.lock pyproject.toml /application/
RUN poetry config virtualenvs.create false \
  && poetry install $(test $ENV == production && echo "--no-dev") --no-interaction --no-ansi

RUN mkdir /application/app
COPY ../app /application/app

COPY ../entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]