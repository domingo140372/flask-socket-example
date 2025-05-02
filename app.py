from flask import Flask, session, redirect, url_for
from extensions import socketio
from modules.index import index_bp
from modules.users import users_bp
from modules.auth import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Necesario para manejar sesiones

# Inicializar extensiones
socketio.init_app(app)

# Registrar los Blueprints
app.register_blueprint(index_bp)
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)

# Ruta principal que redirige al login
@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    socketio.run(app, debug=True)