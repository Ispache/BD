import psycopg2
from prettytable import PrettyTable

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            dbname="tu_base_de_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def ingresar_numeros(numero1, numero2):
    try:
        # Verificar el rango y contar impares
        numeros_impares = [num for num in range(numero1, numero2 + 1) if num % 2 != 0]
        
        print("Listado de números:", *range(numero1, numero2 + 1))
        print("Cantidad de números impares:", len(numeros_impares))

        return numeros_impares
    except Exception as e:
        print(f"Error al ingresar los números: {e}")
        return None

def guardar_historial(conexion, numeros_impares):
    try:
        if numeros_impares:
            cursor = conexion.cursor()

            # Guardar impares en el historial
            for num_impar in numeros_impares:
                cursor.execute("INSERT INTO historial (numero) VALUES (%s);", (num_impar,))

            conexion.commit()
            print("Números ingresados y guardados en el historial.")
    except Exception as e:
        print(f"Error al guardar el historial en la base de datos: {e}")

def ver_historial(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM historial;")
        historial = cursor.fetchall()

        if historial:
            print("Historial de números impares:")
            tabla = PrettyTable()
            tabla.field_names = ["ID", "Número"]
            for registro in historial:
                tabla.add_row([registro[0], registro[1]])
            print(tabla)
        else:
            print("No hay números en el historial.")

    except Exception as e:
        print(f"Error al consultar el historial en la base de datos: {e}")

def main():
    conexion_bd = conectar_bd()

    if conexion_bd:
        while True:
            print("\nMenú:")
            print("1. Ingresar dos números")
            print("2. Ver historial")
            print("3. Salir")

            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "1":
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                numeros_impares = ingresar_numeros(numero1, numero2)
                if numeros_impares:
                    guardar_historial(conexion_bd, numeros_impares)

            elif opcion == "2":
                ver_historial(conexion_bd)

            elif opcion == "3":
                print("Programa finalizado.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        conexion_bd.close()

if __name__ == "__main__":
    main()
