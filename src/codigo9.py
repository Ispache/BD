##Que ingrese un precio en quetzales, e indique cuanto de esa totalidad es IVA y cuanto es el precio sin IVA.
##Considerar que el IVA en Guatemala es el 12% del precio del producto.
##NOTA: Se deberan modificar los campos de la función 'Historial' según la base de datos empleada.

import psycopg2
from tabulate import tabulate
import math

##Los siguientes parámetros deberan ser modificados según la base de datos que se emplee.
def Historial():
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "mapache",
            dbname = "preparatoria"
            )
        cursor = conexion.cursor()
        cursor.execute("SELECT * from ej9;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["figura","area"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")

def Post(area):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "mapache",
            dbname = "preparatoria"
            )
        cursor = conexion.cursor()
        Instruction = "insert into ej9(figura, area) values(%s, %s);"
        valores = (figura, area)
        cursor.execute(Instruction, valores)
        conexion.commit()
        print("Se ha registrado el precio de su producto.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Cuadrado():
    
    lado = int(input("Ingrese el lado del cuadrado: "))     
    area = lado**2
             
    return area



opcion = " "

print(" Calculador AREA")

while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Cuadrado \n'B' Ver historial \n'Z' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='A':
        figura = 'cuadrado'
        numero = Cuadrado()
        Post(numero)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")
    if opcion=='A':
        figura = 'cuadrado'
        numero = Cuadrado()
        Post(numero)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")