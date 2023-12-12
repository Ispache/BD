import psycopg2

# Función para comparar números e imprimir la lista
def comparar_numeros_y_mostrar_lista(numero1, numero2):
    mayor = max(numero1, numero2)
    menor = min(numero1, numero2)

    print(f"El número mayor es: {mayor}")
    print(f"Lista de números del mayor al menor: {list(range(mayor, menor - 1, -1))}")

    # Guardar en la base de datos
    guardar_en_base_de_datos(numero1, mayor)
    guardar_en_base_de_datos(numero2, mayor)

# Función para guardar en la base de datos PostgreSQL
def guardar_en_base_de_datos(ingreso, resultado):
    try:
        # Establecer conexión a la base de datos
        connection = psycopg2.connect(
            user="postgres",
            password="mapache",
            host="localhost",
            port="5432",
            database="preparatoria"
        )
       # print('La conexion fue exitosa')
    #except psycopg2.Error as e:
      #  print('Ocurrio un error en la conexión')
       # print('Verifique sus parámetros')

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Crear la tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                ingreso INTEGER,
                resultado INTEGER
            )
        ''')

        # Insertar datos en la tabla
        cursor.execute('INSERT INTO ej4 (ingreso, resultado) VALUES (%s, %s)', (ingreso, resultado))

        # Confirmar los cambios y cerrar la conexión
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error al trabajar con la base de datos:", error)
    finally:
        # Cerrar la conexión en cualquier caso
        if connection:
            cursor.close()
            connection.close()

# Obtener los números del usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Llamar a la función para comparar y mostrar la lista
comparar_numeros_y_mostrar_lista(numero1, numero2)
