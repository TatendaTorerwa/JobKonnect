#!/usr/bin/python3
"""Creating the database engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import Users, Jobs, Applications, Employees
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

"""Database URL."""
mysql_db_url = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

"""Create database engine."""
engine = create_engine(mysql_db_url)

try:
    conn = engine.connect()
    print('db.connected')
    print('Connection object is :{}'.format(conn))
except Exception as e:
    print('db not connected:', e)

"""Create a session factory."""
Session = sessionmaker(bind=engine)

"""Base class for declarative ORM models."""
Base = declarative_base()

"""Create database tables based on the defined models."""
Base.metadata.create_all(engine)
