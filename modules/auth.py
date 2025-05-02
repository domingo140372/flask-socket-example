from flask import Blueprint, render_template, request, redirect, session, url_for
from modules.users import USERS_DB

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = int(request.form.get('user_id'))
        if user_id in USERS_DB:
            # Guardar el ID del usuario en la sesión
            session['user_id'] = user_id
            return redirect(url_for('index.index'))
        else:
            return "Usuario no encontrado", 404
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))