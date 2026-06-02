
from funciones import *

def main():

    usuario = ""

    while True:

        print("1. Ingresar usuario")
        print("2. Clasificar")
        print("3. Contar caracteres")
        print("4. Buscar carácter")
        print("5. Invertir usuario")
        print("6. Reporte")
        print("7. Simetría")
        print("8. Ordenar")
        print("9. Salir")

        op = input("Opción: ")

        if op == "1":
            usuario = validar_usuario()

        elif op == "2":
            print(clasificar_usuario(usuario))

        elif op == "3":
            contar_caracteres(usuario)

        elif op == "4":
            c = input("Carácter: ")
            buscar_caracter(usuario, c)

        elif op == "5":
            usuario_invertido(usuario)

        elif op == "6":
            reporte(usuario)

        elif op == "7":
            es_simetrico(usuario)

        elif op == "8":
            tipo = input("A (asc) / D (desc): ")
            ordenar(usuario, tipo)

        elif op == "9":
            break

main()