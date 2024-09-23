Aplicación para Mostrar Datos usando python, con framework Django, biblioteca Matplotlib, mysql

Paso 1.
- Crear tu base de datos en mysql8^. llamada: dbdashboard

Paso 2.
- Clona el repositorio:
- Renombra el archivo settings.example.py a settings.py y coloca el usuario y contraseña de tu mysql.
- Ubícate en la misma ruta de manage.py, y ejecuta los siguientes comandos uno por uno:
    python manage.py migrate
    python manage.py makemigrations
    python populate_personas.py 
    
    esto poblará la base de datos.

- Para correr el servidor local, ejecuta el siguiente comando:
    python manage.py runserver








    




