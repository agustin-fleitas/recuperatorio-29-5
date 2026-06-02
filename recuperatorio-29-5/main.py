
from funciones import *

def main():

    usuario = ""

    while True:

        print("\n--- MENU ---")
        print("1. Ingresar usuario")
        print("2. Clasificar usuario")
        print("3. Contar caracteres")
        print("4. Buscar caracter")
        print("5. Invertir usuario")
        print("6. Reporte estadistico")
        print("7. Simetria")
        print("8. Ordenar usuario")
        print("9. Salir")

        op = input("Opcion: ")

        if op == "1":
            usuario = validar_usuario()

        elif op == "2":
            print(clasificar(usuario))

        elif op == "3":
            contar(usuario)

        elif op == "4":
            c = input("Ingrese caracter: ")
            buscar(usuario, c)

        elif op == "5":
            invertir(usuario)

        elif op == "6":
            reporte(usuario)

        elif op == "7":
            simetrico(usuario)

        elif op == "8":
            orden = input("A (asc) / D (desc): ")
            ordenar(usuario, orden)

        elif op == "9":
            break

main()
