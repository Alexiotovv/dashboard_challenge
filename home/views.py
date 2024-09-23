import os
import matplotlib.pyplot as plt
from django.conf import settings
from django.shortcuts import render
from .models import Persona  #Importamos el modelo
from django.db.models import Count
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from home.db_connection import get_db_connection  # Importa la función de conexión


#Vista con Mysql connector

def dashboard_mysqlconnector(request):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    # Obtener datos para el DataTable
    cursor.execute("SELECT * FROM home_persona")  # 
    datos_tabla = cursor.fetchall()

    #### GRÁFICO BARRAS
    # Obtenemos los datos para el gráfico de barras
    cursor.execute("SELECT edad, salario FROM home_persona")
    datos = cursor.fetchall()
    
    # Separamos los datos en listas de edades y salarios
    edades = [dato['edad'] for dato in datos] # usamos un compremhension list
    salarios = [float(dato['salario']) for dato in datos]

    # Creamos el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(edades, salarios, color='blue')

    # Ponemos Etiquetas y título
    ax.set_xlabel('Edad')
    ax.set_ylabel('Salario')
    ax.set_title('Relación entre Edad y Salario')
    
    # Ruta para guardar el gráfico (puedes usar MEDIA_ROOT o STATIC_ROOT)
    grafico_path = os.path.join(settings.MEDIA_ROOT, 'grafico_barras.png')
    
    # Guardar el gráfico en formato PNG
    fig.savefig(grafico_path)
    # Pasar la URL del gráfico generado a la plantilla
    grafico_barras = os.path.join(settings.MEDIA_URL, 'grafico_barras.png')

    #### GRÁFICO CIRCULAR
    # Contar la cantidad de personas por ciudad
    cursor.execute("SELECT ciudad, COUNT(*) as total FROM home_persona GROUP BY ciudad")
    ciudades = cursor.fetchall()

    # Datos para el gráfico circular
    labels = [ciudad['ciudad'] for ciudad in ciudades]
    sizes = [ciudad['total'] for ciudad in ciudades]

    # Crear el gráfico circular
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para que el gráfico sea un círculo

    # Guardar el gráfico en el disco
    graph_path = os.path.join(settings.MEDIA_ROOT, 'grafico_circular.png')
    fig.savefig(graph_path)
    plt.close(fig)  # Cerrar la figura para liberar memoria

    grafico_circular = os.path.join(settings.MEDIA_URL, 'grafico_circular.png')

    # Cerramos el cursor y la conexión
    cursor.close()
    connection.close()

    # Enviamos todo(los 2 graficos y los datos para la tabla)
    return render(request, 'base/dashboard.html', {
        'grafico_barras': grafico_barras,
        'grafico_circular': grafico_circular,
        'datos_tabla': datos_tabla
    })

# Vista para generar el gráfico y guardarlo como archivo
def dashboard(request):
    #Datos para el DataTable
    datos_tabla = Persona.objects.all()
    
    #### GRÁFICO BARRAS
    #Obtener los datos de la tabla Persona
    datos = Persona.objects.all().values_list('edad', 'salario')  #datos para gráfico
    # Separar los datos en listas de edades y salarios
    edades = [dato[0] for dato in datos]
    salarios = [float(dato[1]) for dato in datos]

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(edades, salarios, color='blue')
    
    # Etiquetas y título
    ax.set_xlabel('Edad')
    ax.set_ylabel('Salario')
    ax.set_title('Relación entre Edad y Salario')
    # Ruta para guardar el gráfico (puedes usar MEDIA_ROOT o STATIC_ROOT)
    grafico_path = os.path.join(settings.MEDIA_ROOT, 'grafico_barras.png')
    # Guardar el gráfico en formato PNG
    fig.savefig(grafico_path)
    # Pasar la URL del gráfico generado a la plantilla
    grafico_barras = os.path.join(settings.MEDIA_URL, 'grafico_barras.png')


    #### GRÁFICO CIRCULAR
    # Contar la cantidad de personas por ciudad
    ciudades = Persona.objects.values('ciudad').annotate(total=Count('ciudad'))

    # Datos para el gráfico circular
    labels = [ciudad['ciudad'] for ciudad in ciudades]
    sizes = [ciudad['total'] for ciudad in ciudades]

    # Crear el gráfico circular
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para que el gráfico sea un círculo

    # Guardar el gráfico en el disco
    graph_path = os.path.join(settings.MEDIA_ROOT, 'grafico_circular.png')
    fig.savefig(graph_path)
    plt.close(fig)  # Cerrar la figura para liberar memoria

    grafico_circular = os.path.join(settings.MEDIA_URL, 'grafico_circular.png')


    #Enviamos todo
    return render(request, 'base/dashboard.html', {
        'grafico_barras': grafico_barras,
        'grafico_circular': grafico_circular,
        'datos_tabla':datos_tabla})

