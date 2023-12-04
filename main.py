# Función de actualización de datos
def actualizacion_de_datos():
    print("Actualización de datos...")
    input("Ingrese ticker a pedir: ")
    input("Ingrese fecha de inicio: ")
    input("Ingrese fecha de fin: ")
    print("Pidiendo datos ...")
    print("Datos guardados correctamente")
    
    # Falta pedir los valores a la API y guardar estos datos en una base de datos SQL
def resumen():
    print("Los tickers guardados en la base de datos son: ")
    print("ticker - fecha_inicio <-> fecha_final")
    #for dato in (base_datos):
        #print(f"{ticker} - {fecha_inicio} <-> {fecha_final})
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