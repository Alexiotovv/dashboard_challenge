# home/db_connection.py
import mysql.connector
from django.conf import settings

def get_db_connection():
    try:
        #obtenemos las credenciales para la conexion del archivo settings.py
        connection = mysql.connector.connect(
            host=settings.DATABASES['default']['HOST'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            database=settings.DATABASES['default']['NAME'],
            port=settings.DATABASES['default']['PORT'],
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None