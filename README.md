# Enterprise Full-Stack Application

## Technology Stack
- **Frontend:** React 19, Vite, Tailwind CSS, Material UI, React Router DOM
- **Backend:** Flask (Python 3.11), SQLAlchemy, Flask-Migrate, Flask-JWT-Extended, Flask-Bcrypt
- **Database:** PostgreSQL 16
- **Infrastructure:** Docker & Docker Compose

## Getting Started with Docker
1. Ensure Docker and Docker Compose are installed.
2. Run the following command from the project root:
   ```bash
   docker-compose up --build
   ```
3. Access the Frontend application at `http://localhost:3000` and the Backend API health check at `http://localhost:5000/api/health`.
