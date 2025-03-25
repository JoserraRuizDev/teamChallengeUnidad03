#funciones
import numpy as np

'''
FUNCION QUE ACABA CON EL JUEGO

'''

def abandonar_partida(tablero_jugador):
    confirmacion = input(f"{tablero_jugador.id_usuario}, ¿Estás seguro de que quieres salir del juego? Contesta con YES o NO:")
    if confirmacion.upper() == "YES":
        tablero_jugador.partida_activa = False
    else: 
        print("Continua jugando.")