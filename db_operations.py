#!/usr/bin/env python3
"""
Database operations.
"""

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from base import session 
from db_connector import session
from models.user import User
from sqlalchemy.orm.exc import NoResultFound

session = Session()

"""user routes."""

def add_user_to_db(username, password, role):
    """
    Register a new user in the database.

    Args:
    - username (str): The username of the new user.
    - password (str): The plain text password of the new user.
    - role (str): The role assigned to the new user.

    Returns:
    - None

    Raises:
    - SQLAlchemyError: If there's an error during the database transaction.

    This function hashes the provided plain text password using `generate_password_hash`,
    creates a new `User` object with the provided username, hashed password, and role, 
    and then adds this new user to the database session and commits the transaction.
    """
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

def get_user_by_username(username):
    """
    Retrieve a user from the database by their username.

    Args:
    - username (str): The username of the user to retrieve.

    Returns:
    - User: The user object if found.
    - None: If no user is found, multiple users are found, or a database error occurs.

    Raises:
    - NoResultFound: Exception when no user is found with the given username.
    - MultipleResultsFound: Exception when multiple users are found with the given username.
    - SQLAlchemyError: If there's an error during the database query.

    This function attempts to query the database for a user with the provided username.
    If exactly one user is found, it returns the user object. If no user or multiple users
    are found, or if a database error occurs, it returns `None`.
    """
    try:
        return User.query.filter_by(username=username).one()
    except NoResultFound:
        return None
    except MultipleResultsFound:
        return None
    except SQLAlchemyError:
        return None
 
def get_user_by_id(id):
    """
    Retrieves a user by their ID from the database.

    Args:
    - id (int): The ID of the user to retrieve.

    Returns:
    - User: The user object if found.
    - None: If no user is found with the given ID.

    Raises:
    - NoResultFound: Exception when no user is found with the given ID.
    """
    try:
        user = User.query.get_or_404(id)
        return user
    except NoResultFound:
        return None
