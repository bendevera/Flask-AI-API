import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('api', __name__, url_prefix='/api')

@app.route('/')
def index():
    response = {'success': True, 'message': 'Welcome to the Flask AI API.'}
    return response 
