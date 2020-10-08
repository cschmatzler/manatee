FROM python:3.8-alpine

COPY . /

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE false

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps g++ gcc libffi-dev make musl-dev postgresql-dev

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

RUN apk --purge del .build-deps

ENV MANATEE_ENV production
EXPOSE 8080
CMD [ "uvicorn", "manatee.main:app", "--host", "0.0.0.0", "--port", "8080" ]
