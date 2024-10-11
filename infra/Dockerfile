FROM python:3.12-slim AS base

ARG DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/venv \
    PATH="/venv/bin:${PATH}"
RUN set -eux; env apt-get update; \
    apt-get install -y --no-install-recommends libpq5; \
    rm -rf /var/lib/apt/lists/*
# ---------------------------build------------------------------
FROM base AS build

ARG DEBIAN_FRONTEND=noninteractive
ARG POETRY_VERSION=1.8.3

RUN set -eux; apt-get update; \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev; \
    rm -rf /var/lib/apt/lists/*
RUN set -eux; python -m pip install "poetry==${POETRY_VERSION}"; \
    python -m venv /venv

COPY README.md .
COPY . .
RUN poetry install --no-ansi --no-root --only=main

RUN poetry build -f wheel --no-ansi \
    && python -m pip install --no-deps dist/*.whl
# ----------------------------final-----------------------------
FROM base

COPY --from=build /venv /venv
EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
