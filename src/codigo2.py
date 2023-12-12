# Pedir al usuario que ingrese el número de inicio y el número de fin
Primero = int(input("Ingrese el primer número: "))
Último = int(input("Ingrese el último número: "))

# Imprimir los números de 2 en 2 desde el inicio hasta el fin
for valor in range(Primero, Último + 1, 2):
    print(valor, end=', ')