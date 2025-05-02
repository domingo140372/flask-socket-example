# flask-socket-example
exmaple flask socket io
# Configuración del Entorno Virtual en Python

Este documento describe los pasos necesarios para configurar un entorno virtual en Python y ejecutar las dependencias definidas en el archivo `requirements.txt`.

## Pasos a seguir

1. **Crear un entorno virtual**  
   Ejecuta el siguiente comando para crear un entorno virtual en Python:

   ```bash
   python -m venv venv
   ```

   Esto creará un directorio llamado `venv` que contendrá el entorno virtual.

2. **Activar el entorno virtual**  
   Activa el entorno virtual creado:

   - En sistemas Unix o MacOS:
     ```bash
     source venv/bin/activate
     ```
   - En sistemas Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Instalar las dependencias**  
   Una vez activado el entorno virtual, instala las dependencias especificadas en el archivo `requirements.txt` ejecutando el comando:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar**  
   Asegúrate de que las dependencias se hayan instalado correctamente ejecutando:

   ```bash
   pip list
   ```

5. **Ejecutar la aplicación**  
   Finalmente, ejecuta la aplicación con el siguiente comando:

   ```bash
   python app.py
   ```

¡Listo! Ahora tu entorno virtual está configurado, las dependencias han sido instaladas y tu aplicación está en ejecución.
