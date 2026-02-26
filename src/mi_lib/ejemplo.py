def saluda(nombre):
    print("¡Hola {}!".format(nombre))
    
def tablero(dim, muros):
    filas, columnas = dim
    tab = [[' ' for numero in range(columnas)] for numero in range(filas)]
    for f, c in muros:
        tab[f][c] = 'X'
    tab[0][0] = 'E'
    tab[filas - 1][columnas - 1] = 'S'
    for fila in tab:
        print(fila)
    return tab
def numero_a_palabras(n):

    if n < 0 or n > 999:
        return "El número debe estar entre 0 y 999"

    unidades = {
        0:"cero", 1:"uno", 2:"dos", 3:"tres", 4:"cuatro",
        5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve"
    }

    especiales = {
        10:"diez", 11:"once", 12:"doce", 13:"trece",
        14:"catorce", 15:"quince"
    }

    decenas = {
        20:"veinte", 30:"treinta", 40:"cuarenta",
        50:"cincuenta", 60:"sesenta",
        70:"setenta", 80:"ochenta", 90:"noventa"
    }

    centenas = {
        100:"cien", 200:"doscientos", 300:"trescientos",
        400:"cuatrocientos", 500:"quinientos",
        600:"seiscientos", 700:"setecientos",
        800:"ochocientos", 900:"novecientos"
    }

    if n == 0:
        return "cero"

    palabras = ""

    if n >= 100:
        c = (n // 100) * 100

        if n == 100:
            return "cien"

        if c == 100:
            palabras += "ciento"
        else:
            palabras += centenas[c]

        n = n % 100

        if n != 0:
            palabras += " "


    if 10 <= n <= 15:
        palabras += especiales[n]

    elif 16 <= n <= 19:
        palabras += "dieci" + unidades[n-10]

    elif 20 <= n <= 29:
        if n == 20:
            palabras += "veinte"
        else:
            palabras += "veinti" + unidades[n-20]

    elif n >= 30:
        d = (n // 10) * 10
        palabras += decenas[d]

        if n % 10 != 0:
            palabras += " y " + unidades[n%10]

    elif n > 0:
        palabras += unidades[n]

    return palabras

numero = int(input("Introduce un número entre 0 y 999: "))
resultado = numero_a_palabras(numero)
print("En palabras:", resultado)

palabra = input("Introduce la palabra: ").strip().lower()

while palabra == "":
    palabra = input("La palabra no puede estar vacía. Introduce la palabra: ").strip().lower()

lista_palabra = list(palabra)
letras_restantes = list(palabra)

fallos = 0
letras_acertadas = []
letras_intentadas = []

mensajes = {
    "acierto": "Acierto",
    "fallo": "Fallo",
    "ganar": "Ganaste",
    "perder": "Perdiste"
}

print("\nPalabra:", "*" * len(palabra))

while fallos < 5 and len(letras_restantes) > 0:

    letra = input("\nIntroduce una letra: ").lower()

    # SOLO comprobar que sea 1 carácter
    while len(letra) != 1:
        letra = input("Introduce solo UN carácter: ").lower()

    if letra in letras_intentadas:
        print("Ya intentaste esa letra.")
        continue

    letras_intentadas.append(letra)

    if letra in letras_restantes:
        print(mensajes["acierto"])
        letras_acertadas.append(letra)
        letras_restantes.remove(letra)

        progreso = "".join([l if l in letras_acertadas else "*" for l in lista_palabra])
        print("Palabra:", progreso)

    else:
        print(mensajes["fallo"])
        fallos += 1

if len(letras_restantes) == 0:
    print("\n" + mensajes["ganar"])
else:
    print("\n" + mensajes["perder"])
