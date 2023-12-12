opcion_menu = 0

def mostrar_menu():
    opcion = int(input("Menú principal \n" +
        "1. Iniciar \n" + 
        "2. Salir \n"))
    return opcion

while opcion_menu != 2:
    opcion_menu = mostrar_menu()
    
    if opcion_menu == 1:
        numero_ingresado = int(input("Ingrese un número: "))
        print("\n")
        suma = 0

        for i in range(0, numero_ingresado + 1):
            suma += i

        print(f"La suma de los números del 1 a {numero_ingresado} es: {suma}")
        print("\n")

    elif opcion_menu == 2:
        print("Fin del programa")
