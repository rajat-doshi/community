import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(".env")


def get_database_url() -> str:
    dialect = os.getenv("DB_DIALECT", "mysql").lower()
    db_name = os.getenv("DB_NAME", "community")
    if dialect == "sqlite":
        return f"sqlite:///{db_name}"

    user = os.getenv("DB_USER_NAME", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")

    if password:
        password = quote_plus(password)

    return f"{dialect}+pymysql://{user}:{password}@{host}:{port}/{db_name}"


# Notice we removed the check_same_thread connect_arg (that is only for SQLite)
SQLALCHEMY_DATABASE_URL = get_database_url()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
