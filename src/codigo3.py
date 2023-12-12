# Solicitar al usuario que ingrese un número
entrada_usuario = int(input("Ingrese un número: "))

# Inicializar una lista para almacenar los divisores
lista_divisores = []

# Encontrar los divisores del número
for divisor_candidato in range(1, entrada_usuario + 1):
    if entrada_usuario % divisor_candidato == 0:
        lista_divisores.append(divisor_candidato)

# Mostrar los divisores
print(f"Los divisores de {entrada_usuario} son: {lista_divisores}")
