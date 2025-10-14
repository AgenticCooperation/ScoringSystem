from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.settings import settings

# Database engine
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=settings.debug
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """Database dependency for FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all tables - temporary until Alembic is set up"""
    from app.models import Base
    Base.metadata.create_all(bind=engine)
