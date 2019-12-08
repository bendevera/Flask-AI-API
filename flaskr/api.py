import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for, jsonify
)
from flaskr.db import get_db
# from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created'
        ' FROM post p'
        ' ORDER BY created DESC'
    ).fetchall()
    post_data = []
    for post in posts:
        curr_post = {
            'id': post[0], 
            'title': post[1], 
            'body': post[2], 
            'created': post[3]
            }
        post_data.append(curr_post)
    return jsonify({'success': True, 'message': post_data})

@bp.route('/create', methods=['POST'])
def create():
    print(request.form)
    title = request.form['title']
    body = request.form['body']
    error = None 

    if title is None or title == "":
        error = 'Title can not be null.'
    if body is None or body == "":
        error = 'Body can not be null.'
    if error:
        return jsonify({'success': False, 'message': error})
    else:
        db = get_db()
        db.execute(
            'INSERT INTO post (title, body)'
            ' VALUES (?, ?)',
            (title, body)
        )
        db.commit()
        return jsonify({
            'success': True, 
            'message': 'Post created successfuly'
        })
