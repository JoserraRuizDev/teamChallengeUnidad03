from clases import *
from funciones import *
from variables import *

#print("Bienvenidos a Hundir la Flota")
#print(REGLAS_DEL_JUEGO)

nombre_usuario = "Pepe" #input("Escriba su nombre de usuario")
tablero_jugador = Tablero(nombre_usuario)
tablero_cpu = Tablero(NOMBRE_USUARIO_CPU)

#print(tablero_jugador.disparar_barco_dificil(tablero_cpu.tablero_flota))
#print(tablero_jugador.disparar_barco_facil(tablero_cpu.tablero_flota))

#print(tablero_cpu.dispara_random_facil(tablero_jugador.tablero_sin_barcos))
#print(tablero_cpu.dispara_random_dificil(tablero_jugador.tablero_sin_barcos))

#print(tablero_cpu.tablero_flota)

#tablero_jugador.posicionar_barco_aleatorio()
#tablero_cpu.posicionar_barco_aleatorio()

#print(tablero_jugador.tablero_flota)
tablero_cpu.crear_tablero()
tablero_jugador.crear_tablero()

tablero_jugador.posicionar_barcos(flota_barcos)
tablero_cpu.posicionar_barcos(flota_barcos)

tablero_jugador.dispara_random_facil(tablero_cpu)
tablero_jugador.dispara_random_facil(tablero_cpu)

tablero_cpu.dispara_random_facil(tablero_jugador)
tablero_cpu.dispara_random_dificil(tablero_jugador)
chequeo_vidas(tablero_jugador)