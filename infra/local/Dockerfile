FROM python:3.12.4-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap
RUN apt-get install -y --no-install-recommends netcat

ADD /pyproject.toml .
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

ADD ./infra/local/entrypoint.sh /
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

COPY manage.py .
COPY /src ./src/

ENTRYPOINT ["/entrypoint.sh"]
