FROM python:3.6-alpine as base

FROM base as builder

RUN mkdir /app
RUN apk update && apk add gcc python3-dev musl-dev
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

FROM base

COPY --from=builder /app /usr/local
RUN apk --no-cache add libpq
WORKDIR /app
