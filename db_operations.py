#!/usr/bin/env python3
"""
Database operations.
"""

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from base import SessionLocal
from models.user import User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound




user = User()

"""user routes."""

def register_user(username, password, email, role, phone_number, address,
                 first_name=None, last_name=None, company_name=None, website=None, contact_infor=None):
    """
    Register a new user in the database.

    Args:
    - username (str): The username of the new user.
    - password (str): The plain text password of the new user.
    - role (str): The role assigned to the new user.
    - email(str): The email of the new user.
    - company_name(str): The company name for employers.
    - phone_number(str): Contact details of the user.
    - address(str): Address of the user.
    - first_name(str): The name of the job_seeker.
    - last_name(str): The last name of the job_seeker.
    - website(str): The website of the employer.
    - contact_infor(str): The contact details of the employer.

    Returns:
    - None

    Raises:
    - SQLAlchemyError: If there's an error during the database transaction.

    This function hashes the provided plain text password using `generate_password_hash`,
    creates a new `User` object with the provided username, hashed password, and role, 
    and then adds this new user to the database session and commits the transaction.
    """
    new_user = new_user = User(
        username=username,
        email=email,
        role=role,
        phone_number=phone_number,
        address=address,
        first_name=first_name,
        last_name=last_name,
        company_name=company_name,
        website=website,
        contact_infor=contact_infor
    )

    """Validate role-specific fields."""
    try:
        new_user.validate_role_specific_fields()
    except ValueError as ve:
        raise ValueError(f"Validation error: {str(ve)}")

    print(f"Debugging new_user fields: {new_user.__dict__}")

    """Harsh the password and set."""
    new_user.set_password(password)
    """Add the new user to the database session and commit the transaction."""
    session = SessionLocal()
    try:
        session.add(new_user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f'Failed to register user: {str(e)}')
    finally:
        session.close()


def login_user(email, password):
    """
    Retrieve a user from the database by their email address and validate the password.

    Args:
    - email (str): The email address of the user to retrieve.
    - password (str): The plain text password to verify.

    Returns:
    - User: The user object if login is successful.
    - None: If no user is found with the given email or password does not match.

    Raises:
    - SQLAlchemyError: If there's an error during the database query.

    This function queries the database for a user with the provided email address.
    If found, it verifies the provided password against the stored password hash.
    If both email and password are correct, it returns the user object.
    """
    try:
        session = SessionLocal()
        user = session.query(User).filter_by(email=email).one()
        if user.check_password(password):
            return user
        else:
            return None
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
        session = SessionLocal()
        user = session.query(User).get(id)
        return user
    except NoResultFound:
        return None
