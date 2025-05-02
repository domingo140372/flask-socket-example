from flask import Blueprint, render_template, session, redirect
from flask_socketio import emit, join_room
from extensions import socketio
from modules.users import USERS_DB

index_bp = Blueprint('index', __name__, url_prefix='/')

@socketio.on('connect')
def handle_connect():
    print('Un cliente se ha conectado.')

@socketio.on('join_user_room')
def handle_join_user_room(data):
    user_id = data.get('user_id')
    join_room(user_id)  # Cada usuario tiene su propia "room"
    print(f'El usuario {user_id} se ha unido a su sala.')

@index_bp.route('/')
def index():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/auth/login')

    user = USERS_DB.get(user_id)
    return render_template('index.html', user=user)