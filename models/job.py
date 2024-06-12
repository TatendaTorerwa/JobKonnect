#!/usr/bin/env python3
""" holds class Jobs"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from models.user import User
from sqlalchemy.sql import func

class Job(Base):
    """Represents of Job."""

    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    requirements = Column(Text)
    employer_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    salary = Column(String(50))
    location = Column(String(100))
    job_type = Column(Enum('full-time', 'part-time', 'contract', name='job_type_enum'))
    application_deadline = Column(Date)
    skills_required = Column(Text)
    preferred_qualifications = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())


    employer = relationship('User', back_populates='jobs')
