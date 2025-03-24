#funciones
import numpy as np
'''
CONTADOR DE VIDAS
'''

'''
FUNCION QUE PONE EL TABLERO COMO EN EL INICIO

'''

#def chequeo_vidas(tablero):
 #   cond = tablero[tablero == "O"] # Convierte el tablero en boleanos, True para los que cumplen la condición (=='O')
  #  contador = np.count_nonzero(cond) # el np.count_nonzero() cuenta los valores distintos a cero o los que son True
   # print(f"Te quedan {contador} vidas")

#def chequeo_vidas(tablero):
#    return tablero.contador_vidas

def reiniciar_tablero(tablero):
    no_agua = np.array(tablero.tablero_flota != " ")
    tablero.tablero_flota[no_agua] = " "
    tablero.contador_vidas = 20
    tablero.partida_activa = False
    return tablero.tablero_flota ## + mostrar de nuevo mensaje de bienvenida en pantalla

def reiniciar_partida():
    return

def abandonar_partida(tablero_jugador, tablero_cpu):
    confirmacion = input(f"{tablero_jugador.id_usuario}, ¿Estás seguro de que quieres salir del juego? Contesta con YES o NO:")
    if confirmacion.upper() == "YES":
        reiniciar_tablero(tablero_jugador)
        reiniciar_partida(tablero_cpu)
        print("¡Hasta pronto!")
    else: 
        print("Continua jugando.")
    
def dame_coordenadas():
    coor_1 = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
    coor_2 = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
    disparo = (coor_1, coor_2)
    return disparo

def chequeo_vidas(tablero):  ## SEPARAR CUANDO GANA EL JUGADOR DE CUANDO GANA LA CPU
   if tablero.contador_vidas > 0:
      return tablero.contador_vidas
   else:
      tablero.partida_activa = False
      return 0