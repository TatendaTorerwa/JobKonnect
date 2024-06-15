#!/usr/bin/env python3
"""Creating the database engine and tables."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base, engine
from models.user import User
from models.job import Job
from models.application import Application

""" Create a session factory."""
Session = sessionmaker(bind=engine)

"""Create database tables based on the defined models."""
Base.metadata.create_all(engine)
