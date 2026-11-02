# Full-Stack Application Monorepo

## Technology Stack
- **Frontend:** React 19, TypeScript, Material UI (MUI), Tailwind CSS, React Router DOM
- **Backend:** Flask, Python 3.11, SQLAlchemy, Flask-Migrate, Flask-JWT-Extended, Flask-Bcrypt
- **Database:** PostgreSQL 16
- **Reverse Proxy:** Nginx
- **Containerisation:** Docker & Docker Compose

## Project Structure
```text
project/
  frontend/
  backend/
  database/
  docker/
  docs/
  tests/
  scripts/
  docker-compose.yml
  README.md
```

## Local Development

To run the entire application stack locally using Docker Compose:

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000 (proxied via Nginx on http://localhost:80)
- Backend API: http://localhost:5000
- PostgreSQL: localhost:5432
