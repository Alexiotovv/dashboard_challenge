import os
import django

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appDashboard.settings')  # Reemplaza 'tu_proyecto' con el nombre de tu proyecto
django.setup()

from home.models import Persona  # Asegúrate de importar tu modelo Persona

# Lista de datos para poblar
datos_personas = [
    {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid', 'salario': 3000.00},
    {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Barcelona', 'salario': 3500.00},
    {'nombre': 'Pedro', 'edad': 22, 'ciudad': 'Valencia', 'salario': 2800.00},
    {'nombre': 'María', 'edad': 28, 'ciudad': 'Sevilla', 'salario': 3200.00},
    {'nombre': 'Luis', 'edad': 35, 'ciudad': 'Bilbao', 'salario': 4000.00},
    {'nombre': 'Sara', 'edad': 27, 'ciudad': 'Granada', 'salario': 2900.00},
    {'nombre': 'Jorge', 'edad': 31, 'ciudad': 'Murcia', 'salario': 3700.00},
    {'nombre': 'Laura', 'edad': 26, 'ciudad': 'Zaragoza', 'salario': 3300.00},
    {'nombre': 'Carlos', 'edad': 29, 'ciudad': 'Alicante', 'salario': 3100.00},
    {'nombre': 'Lucía', 'edad': 24, 'ciudad': 'Salamanca', 'salario': 2800.00},
]

# Poblar la tabla
for persona in datos_personas:
    p = Persona(**persona)
    p.save()

print("Datos insertados correctamente.")
