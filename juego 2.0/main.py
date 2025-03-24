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


while tablero_jugador.contador_vidas > 0 or tablero_cpu.contador_vidas > 0:

# HE MOVIDO ESTOS PRINTS PARA QUE SALGAN DESPUÉS DEL DISPARO EN EL TURNO DEL JUGADOR. SE IMPRIMEN EN EL TURNO DE LA CPU SOLO CUANDO GANA
    #print(f"Tablero contador de disparos de la CPU")
    #print(tablero_cpu.tablero_sin_barcos)
    #print(f"Tablero de {tablero_jugador.id_usuario}")
    #print(tablero_jugador.tablero_flota)
    
    print(f"--> TURNO DE {tablero_jugador.id_usuario}:")
    tablero_jugador.dispara_random_facil(tablero_cpu)

    print(f"Tablero rival - comprueba tus disparos a la CPU:")
    print(tablero_cpu.tablero_sin_barcos)
    print(f"Tablero de {tablero_jugador.id_usuario}")
    print(tablero_jugador.tablero_flota)
    if tablero_cpu.contador_vidas == 0:
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
