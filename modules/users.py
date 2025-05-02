from flask import Blueprint, request, render_template, jsonify
from extensions import socketio

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Base de datos simulada de usuarios
USERS_DB = {
    1: {"id": 1, "name": "John Doe", "email": "john@example.com", "password": "hashed_password"},
    2: {"id": 2, "name": "Jane Doe", "email": "jane@example.com", "password": "hashed_password"},
    99: {"id": 99, "name": "Admin", "email": "admin@example.com", "password": "hashed_password"}  # Usuario administrador
}

@users_bp.route('/update_user', methods=['POST'])
def update_user():
    user_id = int(request.form.get('id'))
    new_name = request.form.get('name')
    new_email = request.form.get('email')

    # Actualizar el usuario en la "base de datos"
    if user_id in USERS_DB:
        USERS_DB[user_id].update({"name": new_name, "email": new_email})

        # Emitir una notificación al usuario actualizado
        socketio.emit('user_updated', 
                      {'msg': f'Tu perfil ha sido actualizado, {new_name}. notificion enviada por delegacion a socket'}, 
                      to=str(user_id))
        #emitir notificacion y reultado backend al admin que modifico
        return jsonify({"status": "success", "message": "Usuario actualizad en el admin, el usaurio recibira por socket la notificacion"})

    #emitir notificacion y reultado backend del error al admin
    return jsonify({"status": "error", "message": "Usuario no encontrado, notifiacion resultado directo y no por socket"}), 404

@users_bp.route('/edit/<int:user_id>')
def edit_user(user_id):
    user = USERS_DB.get(user_id)
    if user:
        return render_template('update_user.html', user=user)
    return "Usuario no encontrado", 404