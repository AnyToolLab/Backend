FROM python:3.13.0-alpine3.20

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
    apk add --no-cache jq python3-dev build-base gcc jpeg-dev zlib-dev libpq-dev

COPY Pipfile.lock .
RUN jq -r '.default | to_entries[] | .key + .value.version ' Pipfile.lock > requirements.txt && \
    pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "./entrypoint.sh"]