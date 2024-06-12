#!/usr/bin/env python3
""" holds class Users"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
import bcrypt

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

    def to_dict(self):
        """Converts the User instance to a dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "address": self.address
        }


    def set_password(self, password):
        """Hashes and sets the user's password."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        """Verifies the provided password against the hashed password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
