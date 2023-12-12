import psycopg2

# Función para conectar a la base de datos
def conectar_bd():
    try:
        conexion = psycopg2.connect(
            database="preparatoria",
            user="postgres",
            password="mapache",
            host="localhost",
            port="5432"
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)

# Función para crear la tabla si no existe
def crear_tabla():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Define aquí la estructura de tu tabla si aún no la has creado
    tabla_sql = """
        CREATE TABLE IF NOT EXISTS historial (
            id SERIAL PRIMARY KEY,
            figura VARCHAR(50),
            resultado NUMERIC,
            fecha TIMESTAMP DEFAULT current_timestamp
        );
    """

    cursor.execute(tabla_sql)
    conexion.commit()
    conexion.close()

# Función para calcular el área de un círculo
def area_circulo(radio):
    return 3.14159 * radio ** 2

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return 0.5 * base * altura

# Función para calcular el área de un cuadrado
def area_cuadrado(lado):
    return lado ** 2

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para almacenar el resultado en la base de datos
def guardar_en_bd(figura, resultado):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Insertar el resultado en la tabla historial
    insertar_sql = "INSERT INTO historial (figura, resultado) VALUES (%s, %s);"
    cursor.execute(insertar_sql, (figura, resultado))

    conexion.commit()
    conexion.close()

# Función para mostrar el historial desde la base de datos
def mostrar_historial():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    # Seleccionar todos los registros de la tabla historial
    seleccionar_sql = "SELECT * FROM historial;"
    cursor.execute(seleccionar_sql)

    historial = cursor.fetchall()

    # Mostrar el historial
    for registro in historial:
        print(f"{registro[0]}. Figura: {registro[1]}, Resultado: {registro[2]}, Fecha: {registro[3]}")

    conexion.close()

# Función principal
def main():
    crear_tabla()

    while True:
        print("\nCalculadora de Áreas Geométricas")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Cuadrado")
        print("4. Rectángulo")
        print("5. Mostrar Historial")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            radio = float(input("Ingresa el radio del círculo: "))
            resultado = area_circulo(radio)
            print(f"El área del círculo es: {resultado}")
            guardar_en_bd("Círculo", resultado)
        elif opcion == "2":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            resultado = area_triangulo(base, altura)
            print(f"El área del triángulo es: {resultado}")
            guardar_en_bd("Triángulo", resultado)
        elif opcion == "3":
            lado = float(input("Ingresa el lado del cuadrado: "))
            resultado = area_cuadrado(lado)
            print(f"El área del cuadrado es: {resultado}")
            guardar_en_bd("Cuadrado", resultado)
        elif opcion == "4":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            resultado = area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {resultado}")
            guardar_en_bd("Rectángulo", resultado)
        elif opcion == "5":
            mostrar_historial()
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
