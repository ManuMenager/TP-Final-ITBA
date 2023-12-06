import requests
import json
import sqlite3

# Función de actualización de datos
def actualizacion_de_datos():
    print("Actualización de datos...")
    ticker = input("Ingrese ticker a pedir: ")
    fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese fecha de fin (YYYY-MM-DD): ")
    
    # URL con los parámetros proporcionados por el usuario
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?adjusted=true&sort=asc&limit=120&apiKey=O77plIFbemEZfs7J3bBetBRjKKjkHQlI"
    
    # Hacer la solicitud a la API
    json_file = requests.get(url)
    json_obj = json_file.json()   
    print("Pidiendo datos ...")
        
    # Guardar datos en una base de datos
    guardar_datos_en_db(ticker, fecha_inicio, fecha_fin, json_obj)
    
    #Verificar si la solicitud fue exitosa (Código 200)
    if json_file.status_code == 200:
            print("Datos guardados correctamente")
    else:
        print(f"Error al hacer la solicitud a la API. Código de error: {json_file.status_code}")
    
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

def grafico_ticker():
    input("Ingrese el ticker a graficar: ")
    print("'Aca va el gráfico'")
    #Gráfico con matplotlib
    
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