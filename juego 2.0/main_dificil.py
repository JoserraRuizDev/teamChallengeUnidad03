from clases import *
from funciones import *
from variables import *

print("Bienvenidos a Hundir la Flota")
print(REGLAS_DEL_JUEGO)
nombre_usuario = input("Escriba su nombre de usuario")
tablero_jugador = Tablero(nombre_usuario)
tablero_cpu = Tablero(NOMBRE_USUARIO_CPU)
tablero_jugador.posicionar_barcos(flota_barcos)
tablero_cpu.posicionar_barcos(flota_barcos)

while True:

    print(f"Tablero de la CPU")
    print(tablero_cpu.tablero_sin_barcos)
    print(f"Tablero de {tablero_jugador.id_usuario}")
    print(tablero_jugador.tablero_flota)
    
    tablero_jugador.disparar_barco_facil(tablero_cpu)
    if not tablero_jugador.partida_activa:
        break

    tablero_cpu.dispara_random_dificil(tablero_jugador)