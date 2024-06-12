#!/usr/bin/env python3
""" holds class Employees"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from db_connection import Base
from .models.user import User

class Employee(Base):
    """Represents of Employee."""

    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False, unique=True)
    company_name = Column(String(100), nullable=False)
    website = Column(String(255))
    contact_info = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    user = relationship('User', back_populates='employee')
