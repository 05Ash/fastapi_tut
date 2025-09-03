from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings.config import settings as set

SQLALCHEMY_DATABASE_URL = f'postgresql://{set.database_username}:{set.database_password}@{set.database_address}:{set.database_port}/{set.database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
