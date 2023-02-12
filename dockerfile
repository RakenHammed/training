FROM python:3.10-slim-bullseye

ARG ENVIRONMENT

ENV ENVIRONMENT=${ENVIRONMENT} \
  FLASK_APP="app/__init__.py" \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.1


# System deps:
RUN pip install "poetry==$POETRY_VERSION"
# Copy only requirements to cache them in docker layer
WORKDIR /application
COPY poetry.lock pyproject.toml /application/
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "ENVIRONMENT" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /application

EXPOSE 5000
CMD ["flask", "run"]