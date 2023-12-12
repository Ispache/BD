def comparar_numeros(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        print(f"Los números son: {num1}, {num2}, {num3}. Todos son iguales.")
    elif num1 == num2:
        print(f"El número diferente es: {num3}")
    elif num1 == num3:
        print(f"El número diferente es: {num2}")
    elif num2 == num3:
        print(f"El número diferente es: {num1}")
    else:
        mayor = max(num1, num2, num3)
        if mayor == num1:
            resultado = num1 + num2 + num3
            print(f"El resultado de la suma es: {resultado}")
        elif mayor == num2:
            resultado = num1 * num2 * num3
            print(f"El resultado de la multiplicación es: {resultado}")
        else:
            resultado = str(num1) + str(num2) + str(num3)
            print(f"La concatenación de los números es: {resultado}")

# Pedir los 3 números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para comparar los números
comparar_numeros(numero1, numero2, numero3)
