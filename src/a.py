import psycopg2

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            dbname="preparatoria",
            user="postges",
            password="mapache",
            host="localhost",
            port="5432"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def crear_tabla_historial(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS historial (id SERIAL PRIMARY KEY, figura VARCHAR, resultado DOUBLE PRECISION);")
        conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla en la base de datos: {e}")

def calcular_area_circulo(radio):
    return 3.14159 * radio**2

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_cuadrado(lado):
    return lado**2

def calcular_area_rectangulo(lado1, lado2):
    return lado1 * lado2

def guardar_resultado_en_bd(conexion, figura, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO historial (figura, resultado) VALUES (%s, %s);", (figura, resultado))
        conexion.commit()
        print("Resultado guardado en la base de datos.")
    except Exception as e:
        print(f"Error al guardar el resultado en la base de datos: {e}")

def mostrar_historial_en_consola(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM historial;")
        historial = cursor.fetchall()

        if historial:
            print("Historial de resultados:")
            print("{:<5} {:<10} {:<15}".format("ID", "Figura", "Resultado"))
            print("-" * 30)
            for registro in historial:
                print("{:<5} {:<10} {:<15}".format(registro[0], registro[1], registro[2]))
        else:
            print("No hay registros en el historial.")

    except Exception as e:
        print(f"Error al consultar el historial en la base de datos: {e}")

if __name__ == "__main__":
    conexion_bd = conectar_bd()

    if conexion_bd:
        crear_tabla_historial(conexion_bd)

        print("Calculadora de Áreas:")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Cuadrado")
        print("4. Rectángulo")
        opcion = int(input("Seleccione la figura (1-4): "))

        if opcion == 1:
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            guardar_resultado_en_bd(conexion_bd, "Círculo", area)

        elif opcion == 2:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            guardar_resultado_en_bd(conexion_bd, "Triángulo", area)

        elif opcion == 3:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            guardar_resultado_en_bd(conexion_bd, "Cuadrado", area)

        elif opcion == 4:
            lado1 = float(input("Ingrese el primer lado del rectángulo: "))
            lado2 = float(input("Ingrese el segundo lado del rectángulo: "))
            area = calcular_area_rectangulo(lado1, lado2)
            guardar_resultado_en_bd(conexion_bd, "Rectángulo", area)

        else:
            print("Opción no válida.")

        mostrar_historial_en_consola(conexion_bd)

        conexion_bd.close()
