from clases import *
from funciones import *
from variables import *

print("Bienvenidos a Hundir la Flota")
print(REGLAS_DEL_JUEGO)
nombre_usuario = input("Escriba su nombre de usuario\n")
tablero_jugador = Tablero(nombre_usuario)
tablero_cpu = Tablero(NOMBRE_USUARIO_CPU)
tablero_jugador.posicionar_barcos(flota_barcos)
tablero_cpu.posicionar_barcos(flota_barcos)


while tablero_jugador.contador_vidas > 0 or tablero_cpu.contador_vidas > 0:
    
    print(f"--> TURNO DE {tablero_jugador.id_usuario}:")

    print(f"Tablero rival - comprueba tus disparos a la CPU:")
    print(tablero_cpu.tablero_sin_barcos)
    print(f"Tablero de {tablero_jugador.id_usuario}")
    print(tablero_jugador.tablero_flota)
    tablero_jugador.dispara_manual(tablero_cpu)
    if tablero_cpu.contador_vidas == 0:
        break

    if tablero_jugador.partida_activa is False:
        print("¡Hasta pronto!")
        break

    print("--> TURNO DE LA CPU:")    
    tablero_cpu.dispara_random_facil(tablero_jugador)
    if tablero_jugador.contador_vidas == 0:
        print(f"Tablero de la CPU:")
        print(tablero_cpu.tablero_flota)
        print(f"Tablero de {tablero_jugador.id_usuario}")
        print(tablero_jugador.tablero_flota)
        break

if tablero_cpu.contador_vidas == 0:
    print(f"Enhorabuena, {tablero_jugador.id_usuario}, has ganado.")
elif tablero_jugador.contador_vidas == 0:
    print(f"Lo siento, {tablero_jugador.id_usuario}, has perdido.")
