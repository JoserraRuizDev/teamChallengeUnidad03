from clases import *
from funciones import *
from variables import *

print("Bienvenidos a Hundir la Flota")
print(REGLAS_DEL_JUEGO)

nombre_usuario = "Pepe" #input("Escriba su nombre de usuario")
tablero_jugador = Tablero(nombre_usuario)
tablero_cpu = Tablero(NOMBRE_USUARIO_CPU)

print(tablero_jugador.disparar_barco(tablero_cpu.tablero_flota))
print(tablero_cpu.tablero_flota)

#tablero_jugador.posicionar_barco_aleatorio()
#tablero_cpu.posicionar_barco_aleatorio()

#print(tablero_jugador.tablero_flota)