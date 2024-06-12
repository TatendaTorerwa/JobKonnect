#!/usr/bin/env python3
""" holds class Employees"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from models.user import User
from sqlalchemy.sql import func

class Employee(Base):
    """Represents of Employee."""

    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False, unique=True)
    company_name = Column(String(100), nullable=False)
    website = Column(String(255))
    contact_info = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())

    user = relationship('User', back_populates='employee')

    def to_dict(self):
        """Converts the Employee instance to a dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_name": self.company_name,
            "website": self.website,
            "contact_info": self.contact_info,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
