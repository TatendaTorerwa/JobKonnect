#!/usr/bin/env python3
"""Restful api."""

from flask import Flask, jsonify, request
from flask_cors import CORS
from jwtfunc import generate_token, token_required
from db_operations import *


"""Creating an instance of a flask class."""
app = Flask(__name__)
CORS(app)

"""Route handler for the root URL."""
@app.route('/')
def index():
    """
    Endpoint for the root url.
    """
    return jsonify({'message': 'Welcome to JobKonnect.'})

"""Define routes for user operations."""

@app.route('/api/user/register', methods=['POST'], strict_slashes=False)
def register():
    """
    Endpoint for the user registration.
    """
    """Extract data from JSON request."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role')
    phone_number = data.get('phone_number')
    address = data.get('address')
    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    company_name = data.get('company_name', None)
    website = data.get('website', None)
    contact_infor= data.get('contact_infor', None)

    """Validate required fields based on role."""
    if role == 'job_seeker' and (not first_name or not last_name):
        return jsonify({'error': 'First name and last name are required for job seekers'}), 400
    elif role == 'employer' and (not company_name or not website):
        return jsonify({'error': 'Company name and website are required for employers'}), 400

    try:
        """Call register_user function to add user to database."""
        register_user(username, password, email, role, phone_number, address,
                      first_name=first_name, last_name=last_name,
                      company_name=company_name, website=website, contact_infor=contact_infor)

        return jsonify({'message': 'User registered successfully'}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({'error': f'Failed to register user: {str(se)}'}), 500
    

@app.route('/api/user/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Endpoint for the user login.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    email = data.get('email')
    password = data.get('password')

    """Validate input."""
    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    """Query the user from the database."""
    user = login_user(email, password)
    if user:
        token = generate_token(user.id, user.username, user.role)
        return jsonify({
            'user_id': user.id,
            'token': token
        })
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/user/<int:id>', methods=['GET'], strict_slashes=False)
def get_user_route(id):
    """Implement logic to get user by id."""
    user = get_user_by_id(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

































