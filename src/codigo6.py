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
        entrada_usuario = entrada_usuario.lower()
        vocales = ["a", "e", "i", "o", "u"]

        for vocal in vocales:
            veces = 0
            for caracter in entrada_usuario:
                if vocal == caracter:
                    veces += 1
            print(vocal, "=", veces) 

    elif opcion_menu == 2:
        print("Fin del programa")
