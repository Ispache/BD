import psycopg2
from tabulate import tabulate


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
        cursor.execute("SELECT * from ej11;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["numero1", "numero2","numero3","final"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")

def Post(final):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "mapache",
            dbname = "preparatoria"
            )
        cursor = conexion.cursor()
        Instruction = "insert into ej11(numero1,numero2,numero3,final) values(%s, %s, %s, %s);" 
        valores = (nota1, nota2, nota3, final)
        cursor.execute(Instruction, valores)
        conexion.commit()
        print("Se ha escrito en su DB.")
    except:
        print("Error en el ingreso de datos o de conexion\n")



def nota():
    # Pedir al usuario que ingrese las 3 notas


    # Calcular el promedio de las notas
    promedio = (nota1 + nota2 + nota3) / 3

    # Verificar si el promedio es mayor o igual a 60
    if promedio >= 60:
        final= 'Aprobado'
        print(f"¡Aprobado! El promedio es {promedio:.2f}")
    else:
        final = 'Reprobado'
        print(f"Reprobado. El promedio es {promedio:.2f}")

    return final



opcion = " "

print(" Cuadro de notas")

while opcion != 'x':
    print("Seleccione una opción del siguiente menú: \n'1' Ingresar notas \n'0' Ver historial \n'x' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='1' : 
        nota1 = int(input("Ingrese la primera nota: "))
        nota2 = int(input("Ingrese la segunda nota: "))
        nota3 = int(input("Ingrese la tercera nota: "))
        
        numero = nota()
        Post(numero)
    elif opcion=='0':
        numero = Historial()
        Post(numero)

    elif opcion=='x':
        break
    else:
        print("Opcion no válida, ingrese una de las opciones del menú")