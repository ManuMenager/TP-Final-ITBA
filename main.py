import requests
import json
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Función de actualización de datos
def actualizacion_de_datos():
    print("Actualización de datos...")
    print(" ""1.Ingresar Ticker \n 2.Eliminar Ticker \n 3.Volver atrás")
    actualizacion = int(input("Seleccione una opción (1/2/3): "))

    while True:

            if actualizacion == 1:                
                ingresar_ticker()
                break
            elif actualizacion == 2:
                eliminar_ticker()
                break        
            elif actualizacion == 3:
                break
            else:
                print("Opción inválida. Por favor ingrese una opción válida")
                continue

def ingresar_ticker():    
    ticker = input("Ingrese ticker a pedir: ")
    fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese fecha de fin (YYYY-MM-DD): ")

    # Verificar si el ticker para las fechas dadas ya está en la base de datos
    if ticker_en_db(ticker, fecha_inicio, fecha_fin):
        print(f"Los datos para el ticker {ticker} entre {fecha_inicio} y {fecha_fin} ya están almacenados en la base de datos.")
        return

    api = input("Ingrese su API-KEY de Polygon: ") 
    # URL con los parámetros proporcionados por el usuario
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?adjusted=true&sort=asc&limit=120&apiKey={api}"
    
    # Hacer la solicitud a la API
    json_file = requests.get(url)
    json_obj = json_file.json()   
    print("Pidiendo datos ...")
    
    #Verificar si la solicitud fue exitosa (Código 200)
    if json_file.status_code == 200:
            # Guardar datos en una base de datos
            guardar_datos_en_db(ticker, fecha_inicio, fecha_fin, json_obj)
            print("Datos guardados correctamente")
    else:
        print(f"Error al hacer la solicitud a la API. Código de error: {json_file.status_code}")
        print(ingresar_ticker)

# Función para verificar si un ticker en un rango de fechas ya está en la base de datos
def ticker_en_db(ticker, fecha_inicio, fecha_fin):
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Consultar si el ticker ya está en la base de datos para el rango de fechas dado
    cursor.execute('''
        SELECT COUNT(*) FROM datos WHERE ticker = ? AND fecha_inicio = ? AND fecha_fin = ?
    ''', (ticker, fecha_inicio, fecha_fin))

    count = cursor.fetchone()[0]
    conn.close()

    return count > 0

# Función para eliminar un ticker de la base de datos
def eliminar_ticker():
    ticker = input("Ingrese el ticker a eliminar: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

    if not ticker_en_db(ticker, fecha_inicio, fecha_fin):
        print(f"No hay datos para el ticker {ticker} entre {fecha_inicio} y {fecha_fin} en la base de datos.")
        return

    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Eliminar el ticker de la base de datos para el rango de fechas dado
    cursor.execute('''
        DELETE FROM datos WHERE ticker = ? AND fecha_inicio = ? AND fecha_fin = ?
    ''', (ticker, fecha_inicio, fecha_fin))

    conn.commit()
    conn.close()

    print(f"Los datos para el ticker {ticker} entre {fecha_inicio} y {fecha_fin} han sido eliminados correctamente.")

def guardar_datos_en_db(ticker, fecha_inicio, fecha_fin, datos):
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            datos TEXT
        )
    ''')

    # Insertar los datos en la tabla
    datos = cursor.execute('''
        INSERT INTO datos (ticker, fecha_inicio, fecha_fin, datos)
        VALUES (?, ?, ?, ?)
    ''', (ticker, fecha_inicio, fecha_fin, json.dumps(datos)))

    conn.commit()
    conn.close()
       
# Funcion resumen
def resumen():
    print("Los tickers guardados en la base de datos son: ")
    
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Consultar los datos en la tabla
    cursor.execute('''
        SELECT ticker, fecha_inicio, fecha_fin FROM datos
    ''')

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Imprimir el resumen
    for resultado in resultados:
        ticker, fecha_inicio, fecha_fin = resultado
        print(f"{ticker} - {fecha_inicio} <-> {fecha_fin}")

    conn.close()      

# Función para graficar los datos de un ticker en un rango de fechas
def grafico_ticker():
    ticker = input("Ingrese el ticker a graficar: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Obtener datos del ticker de la base de datos para el rango de fechas dado
    cursor.execute('''
        SELECT fecha_inicio, datos FROM datos WHERE ticker = ? AND fecha_inicio = ? AND fecha_fin = ?
    ''', (ticker, fecha_inicio, fecha_fin))

    result = cursor.fetchone()

    if not result:
        print(f"No hay datos para el ticker {ticker} entre {fecha_inicio} y {fecha_fin} en la base de datos.")
        return

    fecha_inicio, datos_json = result
    conn.close()

    # Convertir datos JSON a DataFrame de pandas
    data = json.loads(datos_json)
    df = pd.DataFrame(data['results'])
    
    # Convertir la columna 't' a formato de fecha
    df['time'] = pd.to_datetime(df['t'], unit='ms')

    # Graficar los datos
    plt.plot(df['time'], df['c'])
    plt.title(f'Variación del precio para {ticker} ({fecha_inicio} - {df["time"].iloc[-1].strftime("%Y-%m-%d")})')
    plt.xlabel('Fecha')
    plt.ylabel('Precio de cierre')
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mejor legibilidad
    plt.show()

    
# Función de visualización de datos
def visualizacion_de_datos():
    print("Visualización de datos...")
    print(" ""1.Resumen \n 2.Gráfico de ticker \n 3.Volver atrás")

    visualizacion = int(input("Seleccione una opción (1/2/3): "))

    while True:

            if visualizacion == 1:                
                resumen()
                break
            elif visualizacion == 2:
                grafico_ticker()
                break        
            elif visualizacion == 3:
                break
            else:
                print("Opción inválida. Por favor ingrese una opción válida")
                continue

while True:
    
    # Menú principal
    inicio = print("Menú Principal:")
    print(" ""1.Actualización de datos \n 2.Visualización de datos \n 3.Salir")

    opcion = int(input("Seleccione una opción (1/2/3): "))
    if opcion == 1:
        actualizacion_de_datos()
    elif opcion == 2:
        visualizacion_de_datos()
    elif opcion == 3:
        print("Hasta luego, gracias por utilizar nuestro programa!")
        break
    else:
        print("Opción inválida. Por favor ingrese una opción válida")
        continue