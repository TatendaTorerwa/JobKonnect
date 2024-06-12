#!/usr/bin/env python3
""" holds class Applications"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from models.user import User
from models.job import Job
from sqlalchemy.sql import func

class Application(Base):
    """Represents of Application."""

    __tablename__ = 'Applications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('Jobs.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    resume = Column(String(255))
    cover_letter = Column(String(255))
    status = Column(Enum('submitted', 'under review', 'rejected', 'accepted', name='status_enum'), default='submitted')
    submitted_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())

    job = relationship('Job', back_populates='applications')
    user = relationship('User', back_populates='applications')
