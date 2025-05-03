# flask-socket-example

Este ejemplo permite aprender como usar la emision de notificaciones masivas.

Emitir un mensaje por salida json implica mantener texto y cookies en ambos lados, 
en el caso de una emision de mensaje por el socket el mensaje esta siempre en el backend 
hasta que se le pide .. una descripcin burda y grotesca pero facil de entender.

## Como empezar

Este documento describe los pasos necesarios para configurar un entorno virtual en Python y ejecutar las dependencias definidas en el archivo `requirements.txt`.

#### iniciando el proyecto

1. **Clonar el repositorio**
   Primero realiza un fork https://github.com/domingo140372/flask-socket-example/fork y despues clona el fork

   ```bash
   mkdir -p ~/Devel

   git clone https://github.com/domingo140372/flask-socket-example
   ```

2. **Crear un entorno virtual**  
   Ejecuta el siguiente comando para crear un entorno virtual en Python:

   ```bash
   cd ~/Devel/flask-socket-example

   python -m venv venv
   ```

   Esto creará un directorio llamado `venv` que contendrá el entorno virtual.

3. **Activar el entorno virtual**  
   Activa el entorno virtual creado:

   - En sistemas Unix o MacOS:
     ```bash
     source venv/bin/activate
     ```
   - En sistemas Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instalar las dependencias**  
   Una vez activado el entorno virtual, instala las dependencias especificadas en el archivo `requirements.txt` ejecutando el comando:

   ```bash
   pip install -r requirements.txt

   pip list
   ```

5. **Ejecutar la aplicación**  
   Finalmente, ejecuta la aplicación con el siguiente comando:

   ```bash
   python app.py
   ```

¡Listo! la aplicacion arrancara en http://127.0.0.1:5000 por defecto!

#### utilizando el sistema

1. **Abre dos navegadores web**  
   ambos abriran la aplicacion en la misma direcion.. 

2. **Navegador 1 ingresar el id 1**
   este usuario recibira una notificacion por socket

3. **Navegador 2 ingresar el id 99**
   est6e usuario es el admin y modificara el usuario 1..

Cuando el admin en el navegador dos modifica el usuario, se envia segun [templates/update_user.html](templates/update_user.html) un emit al socket, y se mantiene en el socket 
mientras que si se enviara en json es para pocos usuarios como el admin .


