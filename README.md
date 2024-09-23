**Título: APP DASHBOARD

**Descripción:
Aplicación para Mostrar Datos usando python, con framework Django, biblioteca Matplotlib, mysql
Obtiene datos de la bdmysql y utiliza la librería matplotlib, para generar gráficos, estos gráficos son guardados, en disco y luego mostrados en el html(front) para visualizarlo

**Requisitos:
python3.10, django4, bootstrap5,mysql8, matplotlib, mysqconnector

**Instalación:
Asegúrate de tener instalado python3.10 en tu pc,
Descargar python3.10 de la página oficial.


Puedes instalar usando entorno virtual o sin entorno virtual.

Crea el entorno virtual, con el siguiente comando:
crea una carpeta para tu proyecto entra y ejecuta el comando:

- En Windows:
    - python -m venv appDashboard_env
    - cd appDashboard_env
    - .\Scripts\activate

- En Linux:
    - virtualenv appDashboard_env
    - cd appDashboard_env
    - source bin/activate


Paso 1.
- Clona el repositorio:
- Renombra el archivo settings.example.py a settings.py y coloca el usuario y contraseña de tu mysql.

Paso 2.
- Crear tu base de datos en mysql. llamada: dbdashboard
- Ubícate en la misma ruta de manage.py, y ejecuta los siguientes comandos uno por uno:
    - python manage.py migrate
    - python manage.py makemigrations
    - python populate_personas.py 
    
    - esto poblará la base de datos.
Paso3.
- Ejecuta el archivo requirements.txt, con el siguiente comando:
    pip install -r requirements.txt

Paso4.
- Para correr el servidor local, ejecuta el siguiente comando:
    - python manage.py runserver

- Abre el navegador y escribe en la barra de url, lo siguiente:
    - localhost:8000/mysql

    Esto mostrará 2 gráficos y una tabla.








    




