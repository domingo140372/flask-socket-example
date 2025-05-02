const socket = io();

// Escuchar notificaciones de actualización de usuario
socket.on('user_updated', (data) => {
    alert(data.msg);
});