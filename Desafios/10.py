# """10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
# numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
# desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
# pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
# desplazarse:
# Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
# una torre, e indique cuál pieza captura a la otra:"""

def coordenadas_tablero(posicion):
    columna = (ord(posicion[0].lower()) - ord("a") + 1) #ord() pasa caracter a numero (a = 97, b = 98, etc), lower() porque a != A, 97 Y 65.
    fila = int(posicion[1])
    return columna, fila

def torre_captura(torre_posicion, alfil_posicion):
    col_torre, fila_torre = coordenadas_tablero(torre_posicion)
    col_alfil, fila_alfil = coordenadas_tablero(alfil_posicion)

    return col_torre == col_alfil or fila_torre == fila_alfil

def alfil_captura(torre_posicion, alfil_posicion):
    col_torre, fila_torre = coordenadas_tablero(torre_posicion)
    col_alfil, fila_alfil = coordenadas_tablero(alfil_posicion)
    
    return abs(col_torre-col_alfil) == abs(fila_torre-fila_alfil)

def captura(torre_posicion, alfil_posicion):
    if alfil_captura(torre_posicion, alfil_posicion):
        return "El Alfil captura a la Torre."
    elif torre_captura(torre_posicion, alfil_posicion):
        return "La Torre captura al Alfil."
    else:
        return "Ninguno se puede capturar"
    

torre_posicion = input("Defina la posicion de la Torre: ")
alfil_posicion = input("Defina la posicion del Alfil: ")

resultado = captura(torre_posicion, alfil_posicion)

print(resultado)