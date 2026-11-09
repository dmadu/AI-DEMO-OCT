# Project 45

Production-ready monorepo scaffold implementing a clean, layered architecture with a
Flask (Python 3.11) REST API, a React 19 + TypeScript single page application, a
PostgreSQL 16 database and an Nginx reverse proxy, orchestrated with Docker Compose.

---

## Table of contents

- [Technology stack](#technology-stack)
- [Project structure](#project-structure)
- [Architecture](#architecture)
- [Quick start (Docker Compose)](#quick-start-docker-compose)
- [Local development without Docker](#local-development-without-docker)
- [Environment configuration](#environment-configuration)
- [Database](#database)
- [Testing](#testing)
- [Scripts](#scripts)
- [Documentation](#documentation)

---

## Technology stack

| Layer            | Technology                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Frontend         | React 19, TypeScript, Material UI (MUI), Tailwind CSS, React Router |
| Backend          | Python 3.11, Flask, Flask-JWT-Extended, Flask-Bcrypt               |
| Database         | PostgreSQL 16, SQLAlchemy 2, Flask-Migrate (Alembic)               |
| Containerisation | Docker, Docker Compose, Nginx                                      |
| CI/CD            | Git, Jenkins                                                        |

No other third-party runtime dependencies are introduced.

---

## Project structure

```text
project_45/
├── backend/                   # Flask REST API (clean architecture)
│   ├── app/
│   │   ├── api/               # Controller / API layer (blueprints, versioned)
│   │   │   └── v1/
│   │   ├── core/              # Cross-cutting concerns (logging, errors, security)
│   │   ├── models/            # SQLAlchemy ORM models (database layer)
│   │   ├── repositories/      # Repository layer (data access)
│   │   ├── schemas/           # Input validation / serialisation helpers
│   │   ├── services/          # Service layer (business logic)
│   │   ├── config.py          # Environment based configuration
│   │   └── extensions.py      # Flask extension singletons
│   ├── migrations/            # Flask-Migrate (Alembic) revisions
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── requirements.txt
│   └── wsgi.py                # WSGI entrypoint (gunicorn)
├── frontend/                  # React 19 + TypeScript SPA (presentation layer)
│   ├── src/
│   │   ├── api/               # Typed API client
│   │   ├── components/        # Reusable UI components
│   │   └── pages/             # Routed pages
│   ├── Dockerfile
│   ├── nginx.conf             # Static file server for the built SPA
│   └── package.json
├── database/                  # PostgreSQL bootstrap and seed SQL
│   ├── init/                  # Executed on first container start
│   └── seeds/                 # Optional seed data
├── docker/                    # Container support files
│   └── nginx/default.conf     # Reverse proxy configuration
├── docs/                      # Installation, API, deployment, architecture docs
├── scripts/                   # Developer helper scripts
├── tests/                     # Unit, integration and API tests (pytest)
├── docker-compose.yml         # Production-like orchestration
├── docker-compose.dev.yml     # Development overrides (hot reload)
├── Jenkinsfile                # CI/CD pipeline
└── .env.example               # Environment configuration template
```

---

## Architecture

```text
Presentation Layer      React 19 SPA (frontend/src)
        ↓ HTTPS/REST
Controller / API Layer  Flask blueprints (backend/app/api)
        ↓
Service Layer           Business rules (backend/app/services)
        ↓
Repository Layer        Data access (backend/app/repositories)
        ↓
Database                PostgreSQL 16 via SQLAlchemy
```

- Each layer depends only on the layer directly beneath it (Dependency Inversion).
- Repositories and services are injected through constructors, keeping controllers thin
  and the business logic unit-testable without a web context.
- Cross-cutting concerns (logging, error translation, security headers, request
  correlation IDs) live in `backend/app/core` and are registered once by the application
  factory.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for details.

---

## Quick start (Docker Compose)

### Prerequisites

- Docker Engine 24+
- Docker Compose v2 (`docker compose`)

### 1. Create the environment file

```bash
cp .env.example .env
# or generate strong secrets automatically:
bash scripts/bootstrap.sh
```

### 2. Validate the orchestration file

```bash
docker compose config
```

### 3. Build and start the stack

```bash
docker compose up --build -d
```

| Service  | URL / Port                        | Description                       |
| -------- | --------------------------------- | --------------------------------- |
| nginx    | http://localhost:8080             | Reverse proxy (single entrypoint) |
| frontend | internal `frontend:80`            | Static React build                |
| backend  | internal `backend:5000`           | Flask REST API (`/api/v1`)        |
| db       | internal `db:5432`                | PostgreSQL 16                     |

Health check: <http://localhost:8080/api/v1/health>

### 4. Stop the stack

```bash
docker compose down          # keep data
docker compose down -v       # also remove the database volume
```

### Development mode (hot reload)

```bash
bash scripts/dev.sh
# equivalent to:
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

In development mode the Vite dev server (port `5173`) and the Flask reloader are used,
source directories are bind-mounted and PostgreSQL is published on the host.

---

## Local development without Docker

### Backend

```bash
cd backend
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
export $(grep -v '^#' ../.env | xargs)   # or export variables manually
flask --app wsgi:app run --debug --port 5000
```

### Frontend

```bash
cd frontend
npm install
npm run dev          # http://localhost:5173 (proxies /api to the backend)
```

---

## Environment configuration

All secrets and environment specific values are read from environment variables; nothing
is hardcoded. Start from [`.env.example`](.env.example):

| Variable                           | Description                                   |
| ---------------------------------- | --------------------------------------------- |
| `APP_ENV`                          | `development`, `testing` or `production`      |
| `SECRET_KEY`                       | Flask session/signing key (min. 32 chars)     |
| `JWT_SECRET_KEY`                   | JWT signing key (min. 32 chars)               |
| `POSTGRES_*`                       | Database name, user, password, host, port     |
| `DATABASE_URL`                     | Optional full SQLAlchemy URL (overrides above)|
| `BCRYPT_LOG_ROUNDS`                | Password hashing cost (>= 12 recommended)     |
| `LOG_LEVEL`                        | `DEBUG`/`INFO`/`WARNING`/`ERROR`              |
| `NGINX_HTTP_PORT`                  | Published host port for the reverse proxy     |
| `VITE_API_BASE_URL`                | API base path used by the SPA build           |

`.env` is git-ignored — never commit real secrets.

---

## Database

- Schema bootstrap SQL in `database/init` runs automatically the first time the
  PostgreSQL volume is created.
- Application schema changes are managed with Flask-Migrate:

```bash
docker compose exec backend flask db init      # once, if migrations/ is empty
docker compose exec backend flask db migrate -m "create users"
docker compose exec backend flask db upgrade
```

The backend entrypoint runs `flask db upgrade` automatically when a migrations