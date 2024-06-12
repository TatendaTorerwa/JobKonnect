#!/usr/bin/env python3
""" holds class Users"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from models.application import Application
from models.employee import Employee

class User(Base):
    """Represents of User."""

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(Enum('job_seeker', 'employer', name='role_enum'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(15))
    address = Column(String(255)) 

    applications = relationship('Application', back_populates='user')
    employee = relationship('Employee', back_populates='user')
