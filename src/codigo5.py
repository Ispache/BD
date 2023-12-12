opcion_menu = 0

def mostrar_menu():
    opcion = int(input("Menú principal \n" +
        "1. Iniciar \n" + 
        "2. Salir \n"))
    return opcion

while opcion_menu != 2:
    opcion_menu = mostrar_menu()
    
    if opcion_menu == 1:
        entrada_usuario = input("Ingrese una palabra o frase: ")
        contador_vocales = 0

        for caracter in entrada_usuario:
            if caracter in "aeiouáéíóú":
                contador_vocales += 1

        print("La cantidad de vocales es: ", contador_vocales)

    elif opcion_menu == 2:
        print("Fin del programa")
