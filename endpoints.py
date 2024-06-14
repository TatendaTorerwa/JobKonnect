#!/usr/bin/env python3
"""Restful api."""

from flask import Flask, jsonify, request
from falsk_cors import CORS
from helper_routes import generate_token, token_required
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
    return jsonify({'message': 'Welcome to JobKonnect.')}

"""Define routes for user operations."""

@app.route('/api/register', methods=['POST'], strictslashes=False)
def register():
    """
    Endpoint for the user registration.
    """
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data['role']

    add_user_to_db(username, password, role)
    
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/api/user/login', methods=['POST'])
def login_user():
    """
    Endpoint for the user login.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Query the user from the database
    user = get_user_by_username(username)
    if user and user.check_password(password):
        token = generate_token(user.id, user.username, user.role)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/user/<int:id>', methods=['GET'])
def get_user_route(id):
    """Implement logic to get user by id."""
    user = get_user_by_id(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())


















































