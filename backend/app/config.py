"""Application configuration objects.

Every configuration value is resolved from environment variables so that no
credential or secret is ever hard-coded in the code base.  Configuration
objects are instantiated at application creation time which keeps the
resolution lazy and makes the behaviour easy to test.
"""

from __future__ import annotations

import os
import secrets
from datetime import timedelta
from typing import Any, Final
from urllib.parse import quote_plus, urlsplit, urlunsplit

from sqlalchemy.pool import StaticPool

from app.core.exceptions import ConfigurationError

DEFAULT_POSTGRES_DRIVER: Final[str] = "postgresql+psycopg2"
DEFAULT_TEST_DATABASE_URI: Final[str] = "sqlite+pysqlite:///:memory:"
_TRUTHY: Final[frozenset[str]] = frozenset({"1", "true", "yes", "on"})


def env_str(name: str, default: str | None = None) -> str | None:
    """Return a stripped environment variable or ``default`` when unset/blank."""
    raw = os.getenv(name)
    if raw is None:
        return default
    raw = raw.strip()
    return raw if raw else default


def env_bool(name: str, default: bool = False) -> bool:
    raw = env_str(name)
    if raw is None:
        return default
    return raw.lower() in _TRUTHY


def env_int(name: str, default: int) -> int:
    raw = env_str(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError as exc:  # pragma: no cover - defensive
        raise ConfigurationError(
            f"Environment variable '{name}' must be an integer, got '{raw}'."
        ) from exc


def normalise_database_url(url: str) -> str:
    """Force an explicit, supported PostgreSQL driver on the connection URL.

    ``postgres://`` (used by several hosting providers) is not understood by
    SQLAlchemy 2.x, and the bare ``postgresql://`` scheme relies on the default
    driver.  Both are rewritten to ``postgresql+psycopg2://``.
    """
    parts = urlsplit(url)
    if parts.scheme in {"postgres", "postgresql"}:
        return urlunsplit(
            (
                DEFAULT_POSTGRES_DRIVER,
                parts.netloc,
                parts.path,
                parts.query,
                parts.fragment,
            )
        )
    return url


def build_postgres_uri_from_parts() -> str:
    "