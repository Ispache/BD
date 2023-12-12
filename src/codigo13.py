import psycopg2
from psycopg2 import sql
from tabulate import tabulate


# Conexión a la base de datos PostgreSQL (asegúrate de cambiar los valores)
conexion = psycopg2.connect(
    dbname="preparatoria",
    user="postgres",
    password="mapache",
    host="localhost",
    port="5432"
)

def es_bisiesto(anio):
    # Función para verificar si un año es bisiesto
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def insertar_en_historial(anio, bisiesto):
    # Función para insertar un registro en la base de datos
    with conexion.cursor() as cursor:
        cursor.execute(sql.SQL("""
            INSERT INTO ej13 (anio, bisiesto)
            VALUES (%s, %s)
        """), (anio, bisiesto))
    conexion.commit()

def mostrar_historial():
    try:
        
        conexion = psycopg2.connect(
            user="postgres",
            password="mapache",
            host="localhost",
            port="5432",
            database="preparatoria"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ej13")

        print(tabulate(cursor, headers=["anio", "bisiesto"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")
def main():
    while True:
        try:
            # Menú principal
            print("1. Verificar si un año es bisiesto")
            print("2. Mostrar historial")
            print("0. Salir")

            opcion = int(input("Ingrese su opción: "))

            if opcion == 1:
                # Verificar si un año es bisiesto
                anio = int(input("Ingrese el año de nacimiento: "))
                bisiesto = es_bisiesto(anio)
                print(f"El año {anio} {'es' if bisiesto else 'no es'} bisiesto.")
                insertar_en_historial(anio, bisiesto)

            elif opcion == 2:
                # Mostrar historial
                mostrar_historial()

            elif opcion == 0:
                # Salir del programa
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    try:
        main()
    finally:
        # Cerrar la conexión a la base de datos al salir
        conexion.close()
