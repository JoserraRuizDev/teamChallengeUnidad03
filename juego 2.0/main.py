from clases import *
from funciones import *
from variables import *

print("Bienvenidos a Hundir la Flota")
print(REGLAS_DEL_JUEGO)
nombre_usuario = "User" #input("Escriba su nombre de usuario")
tablero_jugador = Tablero(nombre_usuario)
tablero_cpu = Tablero(NOMBRE_USUARIO_CPU)

while True:
    
    tablero_jugador.disparar_barco_facil(tablero_cpu)
    if not tablero_jugador.partida_activa:
        break 

    tablero_cpu.dispara_random_facil(tablero_jugador)