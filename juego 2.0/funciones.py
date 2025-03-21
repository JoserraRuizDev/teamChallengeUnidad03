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

def reiniciar_partida(tablero):
    no_agua = np.array(tablero.tablero_flota != " ")
    tablero.tablero_flota[no_agua] = " "
    tablero.contador_vidas = 20
    return tablero.tablero_flota ## + mostrar de nuevo mensaje de bienvenida en pantalla

def abandonar_partida(tablero):
    confirmacion = input("¿Estás seguro de que quieres salir del juego? Contesta con YES o NO:")
    if confirmacion.upper() == "YES":
        no_agua = np.array(tablero.tablero_flota != " ")
        tablero.tablero_flota[no_agua] = " "
        tablero.contador_vidas = 20
        return "¡Hasta pronto!"
    else: 
        return "Continua jugando."
    
def dame_coordenadas():
    coor_1 = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
    coor_2 = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
    disparo = (coor_1, coor_2)
    return disparo

def chequeo_vidas(tablero):
   if tablero.contador_vidas > 0:
      return tablero.contador_vidas
   else:
      return "No te quedan más vidas, fin del juego!"



#def reinicio_juego(tablero):
 #   tablero.where(tablero == "X","O", tablero)
  #  return tablero