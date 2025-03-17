#funciones
import numpy as np
'''
CONTADOR DE VIDAS
'''

'''
FUNCION QUE PONE EL TABLERO COMO EN EL INICIO

'''

def chequeo_vidas(tablero):
    cond = tablero[tablero == "O"] # Convierte el tablero en boleanos, True para los que cumplen la condición (=='O')
    contador = np.count_nonzero(cond) # el np.count_nonzero() cuenta los valores distintos a cero o los que son True
    print(f"Te quedan {contador} vidas")


def reinicio_juego(tablero):
    tablero.where(tablero == "X","O", tablero)
    return tablero