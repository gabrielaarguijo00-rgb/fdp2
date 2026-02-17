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
