def validar_usuario():

    bandera = "N"
    usuario = ""

    while bandera == "N":

        usuario = input("Ingrese usuario: ")

        valido = "S"

        if usuario == "":
            print("No puede estar vacío.")
            valido = "N"
            
    
        if valido == "S":
            if len(usuario) < 6 or len(usuario) > 15:
                print("Debe tener entre 6 y 15 caracteres.")
                valido = "N"

        if valido == "S":
            if 48 <= ord(usuario[0]) <= 57:
                print("No puede comenzar con número.")
                valido = "N"

        tiene_letra = "N"

        if valido == "S":

            for c in usuario:

                ascii_c = ord(c)

                if c == " ":
                    print("No puede tener espacios.")
                    valido = "N"
                    break

                if (65 <= ascii_c <= 90) or (97 <= ascii_c <= 122):
                    tiene_letra = "S"

                elif 48 <= ascii_c <= 57:
                    valido = "S"

                elif ascii_c == 95 or ascii_c == 46:
                    valido = "S"

                else:
                    print("Caracter no permitido.")
                    valido = "N"
                    break

        if tiene_letra == "N" and valido == "S":
            print("Debe tener al menos una letra.")
            valido = "N"

        if valido == "S":
            bandera = "S"

    return usuario


def clasificar(usuario):

    letras = 0
    numeros = 0
    simbolos = 0

    for c in usuario:

        ascii_c = ord(c)

        if (65 <= ascii_c <= 90) or (97 <= ascii_c <= 122):
            letras += 1

        elif 48 <= ascii_c <= 57:
            numeros += 1

        elif ascii_c == 95 or ascii_c == 46:
            simbolos += 1

    if numeros == 0 and simbolos == 0 and len(usuario) >= 6 and len(usuario) <= 8:
        return "Básico"

    if numeros > 0 and simbolos == 0 and len(usuario) >= 8:
        return "Intermedio"

    if numeros > 0 and simbolos > 0 and len(usuario) >= 12:
        ultimo = ord(usuario[len(usuario) - 1])

        if ultimo != 95 and ultimo != 46:
            return "Avanzado"

    return "Sin categoría"


def contar(usuario):

    letras = 0
    numeros = 0
    guion = 0
    punto = 0

    for c in usuario:

        ascii_c = ord(c)

        if (65 <= ascii_c <= 90) or (97 <= ascii_c <= 122):
            letras += 1

        elif 48 <= ascii_c <= 57:
            numeros += 1

        elif ascii_c == 95:
            guion += 1

        elif ascii_c == 46:
            punto += 1

    print("Letras:", letras)
    print("Numeros:", numeros)
    print("Guion bajo:", guion)
    print("Puntos:", punto)


def buscar(usuario, caracter):

    contador = 0
    posiciones = ""

    for i in range(len(usuario)):

        if ord(usuario[i]) == ord(caracter):
            contador += 1
            posiciones += str(i) + " "

    print("Veces que aparece:", contador)
    print("Posiciones:", posiciones)


def invertir(usuario):

    invertido = ""

    for i in range(len(usuario) - 1, -1, -1):
        invertido = invertido + usuario[i]

    print("Original:", usuario)
    print("Invertido:", invertido)


def reporte(usuario):

    letras = 0
    numeros = 0
    simbolos = 0
    repetidos = 0

    i = 0

    while i < len(usuario):

        c = usuario[i]
        ascii_c = ord(c)

        if (65 <= ascii_c <= 90) or (97 <= ascii_c <= 122):
            letras += 1

        elif 48 <= ascii_c <= 57:
            numeros += 1

        else:
            simbolos += 1

        if i < len(usuario) - 1:
            if usuario[i] == usuario[i + 1]:
                repetidos += 1

        i += 1

    total = len(usuario)

    print("\n--- REPORTE ---")
    print("Longitud:", total)

    print("Porcentaje letras:", (letras * 100) / total)
    print("Porcentaje numeros:", (numeros * 100) / total)
    print("Porcentaje simbolos:", (simbolos * 100) / total)

    print("Repetidos consecutivos:", repetidos)


def simetrico(usuario):

    n = len(usuario)

    # si la longitud es impar, no se puede dividir en dos mitades exactas
    if n % 2 != 0:
        print("No tiene dos mitades iguales")
        return

    mitad = n // 2

    primera = ""
    segunda = ""

    for i in range(mitad):
        primera = primera + usuario[i]

    for i in range(mitad, n):
        segunda = segunda + usuario[i]

    if primera == segunda:
        print("Las mitades son iguales")
    else:
        print("Las mitades no son iguales")

def ordenar(usuario, orden):

    lista = []

    for c in usuario:
        lista = lista + [c]

    n = len(lista)

    for i in range(n):

        for j in range(n - 1):

            if orden == "A":
                if ord(lista[j]) > ord(lista[j + 1]):
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux

            else:
                if ord(lista[j]) < ord(lista[j + 1]):
                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux

    resultado = ""

    for c in lista:
        resultado = resultado + c

    print("Ordenado:", resultado)





