#!/usr/bin/env python3
""" holds class Users"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class User(Base):
    """Represents of User."""

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(Enum('job_seeker', 'employer', name='role_enum'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=sqlalchemy.func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now())
    first_name = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(15))
    address = Column(String(255)) 

