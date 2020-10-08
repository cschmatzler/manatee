FROM python:3.8-alpine

WORKDIR /usr/src/app
COPY . /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE false

ENV MANATEE_ENV production

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps g++ gcc libffi-dev make musl-dev postgresql-dev

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

RUN apk --purge del .build-deps

CMD [ "uvicorn", "manatee.main:app", "--host", "0.0.0.0", "--port", "20000" ]
