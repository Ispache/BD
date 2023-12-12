# Solicitar al usuario que ingrese dos números
entrada_usuario1 = int(input("Ingrese el primer número: "))
entrada_usuario2 = int(input("Ingrese el segundo número: "))

# Determinar cuál es el mayor de los dos números
numero_mayor = max(entrada_usuario1, entrada_usuario2)
numero_menor = min(entrada_usuario1, entrada_usuario2)

# Crear la lista de números desde el mayor hasta el menor
lista_numeros = list(range(int(numero_mayor), int(numero_menor) - 1, -1))

# Mostrar la lista de números
print(f"Lista de números desde {numero_mayor} hasta {numero_menor}: {lista_numeros}")
