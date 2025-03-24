#clases
import random
import numpy as np
from variables import flota_barcos
from funciones import *

class Tablero:
    def __init__(self, nombre_usuario):
        self.id_usuario = nombre_usuario
        self.barcos = flota_barcos
        self.tablero_sin_barcos = Tablero.crear_tablero()
        self.tablero_flota = Tablero.crear_tablero() # nuestro tablero
        self.contador_vidas = 20
        self.partida_activa = True

    @staticmethod
    def crear_tablero(relleno = " "):
        # genero tablero
        return np.full((10,10), relleno)

    def posicionar_barcos(self, flota_barcos):
        #Condicion para que se cree un bucle que pase por todos los valores de la flota 
        # de barcos hasta que estén todos los barcos colocados
        for eslora in flota_barcos.values():
            posicionado = False
            while(not posicionado):
                _, resultado = self.posicionar_barco_aleatorio(eslora) # va a la funcion posicionar barco aleatorio
                posicionado = resultado == "Barco posicionado"
    
        print (f"Flota {self.id_usuario} posicionada")

    def posicionar_barco_aleatorio(self, eslora):
        # Generar coordenada inicial aleatoria randint(0, 9)
        fila_inicial = random.randint(0, self.tablero_flota.shape[0] - 1)
        columna_inicial = random.randint(0, self.tablero_flota.shape[1] - 1)
        orientacion = random.choice(['N', 'E', 'S', 'O'])
        # Calcular coordenada final según orientación
        if orientacion == 'N':
            fila_final = fila_inicial - (eslora - 1)
            columna_final = columna_inicial
        elif orientacion == 'E':
            fila_final = fila_inicial
            columna_final = columna_inicial + (eslora - 1)
        elif orientacion == 'S':
            fila_final = fila_inicial + (eslora - 1)
            columna_final = columna_inicial
        else:
            fila_final = fila_inicial
            columna_final = columna_inicial - (eslora - 1)
        
        #print("Posicionando en: " + str((fila_inicial, columna_inicial)) + ", " + str((fila_final, columna_final)) + " orientacion " + orientacion)
        #una vez originadas las coordenadas y la orientación de manera aleatoria, 
        # llamamos a la función posicionar barco con orientación
        return self.posicionar_barco_con_orientacion((fila_inicial, columna_inicial), (fila_final, columna_final))

    #Función que sirve para comprobar si las coordenadas de mi barco no se salen del tablero
    #  y si se pueden posicionar ( comprobar si no hay otro barco ya)
    def posicionar_barco_con_orientacion(self, coordenada_inicial, coordenada_final, relleno = "O"):
        # posiciono los barcos en el tablero en coordenada_inicial y coordenada_final ambas incluídas con orientacion
        fila_inicial = coordenada_inicial[0]
        fila_final = coordenada_final[0]
        columna_inicial = coordenada_inicial[1]
        columna_final = coordenada_final[1]
        # Comprobar que la coordenada inicial entra en el tablero
        if (fila_inicial < 0
            or fila_inicial >= self.tablero_flota.shape[0]
            or columna_inicial < 0
            or columna_inicial >= self.tablero_flota.shape[1]):
            return (self.tablero_flota, "No se puede posicionar: coordenada inicial fuera del tablero")
        
        # Comprobar que la coordenada final entra en el tablero
        if (fila_final < 0
            or fila_final >= self.tablero_flota.shape[0]
            or columna_final < 0
            or columna_final >= self.tablero_flota.shape[1]):
            return (self.tablero_flota, "No se puede posicionar: coordenada final fuera del tablero")

        # Obtener recorrido de la orientacion de las filas
        if (fila_inicial < fila_final):
            recorrido_fila = range(fila_inicial, fila_final + 1)
        else:
            recorrido_fila = range(fila_inicial, fila_final - 1, -1)

        # Obtener recorrido de la orientacion de las columnas
        if (columna_inicial < columna_final):
            recorrido_columna = range(columna_inicial,columna_final + 1)
        else:
            recorrido_columna = range(columna_inicial, columna_final - 1, -1)

        # Copia del tablero para evitar modificar el original 
        #  en caso de que al ir colocando las esloras, haya una que no puedas colocar porque 
        #  haya ya otro barco anteriormente colocado
        tablero_resultante = np.copy(self.tablero_flota)
        for i in recorrido_fila:
            for j in recorrido_columna:
                if (tablero_resultante[i,j] == relleno):
                    return (tablero_resultante, "No se puede posicionar: Coordenadas ocupadas")
                else:
                    tablero_resultante[i,j] = relleno
        self.tablero_flota = tablero_resultante
        
        return (self.tablero_flota, "Barco posicionado")



    
    """"
    FUNCION DISPARAR DE MODO ALEATORIO:

    NIVEL FACIL

    """

    def dispara_random_facil(self, tablero): 
        intentos = 1
        while intentos > 0:
            intentos -= 1
            fila = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
            columna = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
            sitio = (fila, columna)
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.contador_vidas -= 1
                chequeo_vidas(tablero)
                print(f"¡Tocado! Has acertado disparando a la coordenada {sitio}.")
                print(f"Le quedan {chequeo_vidas(tablero)} vidas a su oponente.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X":
                print("Ya has disparado en esta coordenada, dispara de nuevo")
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                print(f"¡Agua! Has disparado a la coordenada {sitio}.")

        return (tablero.tablero_flota, tablero.contador_vidas)
    
    '''
    FUNCION DISPARAR DE MODO ALEATORIO:

    MODO DIFICL ()
    '''

    def dispara_random_dificil(self, tablero):
        intentos = 2
        disparos_agua = 0
        while intentos > 0 and disparos_agua < 2:
            intentos -= 1
            coor_1 = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
            coor_2 = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
            sitio = (coor_1, coor_2) 
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.contador_vidas -= 1
                print("Has disparado a un barco")
                print(f"Le quedan {chequeo_vidas(tablero)} vidas a su oponente.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X":
                print("Intenta en otro sitio")
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                print("Disparo en agua")
                intentos +=1
                disparos_agua += 1
                if disparos_agua == 2:
                    print("has alcanzado el numero maximo de intentos")

        return tablero
    
    '''
    DISPARO MANUAL PARA USUARIO, SI HAS DISPARADO ANTES TE VUELVE A PREGUNTAR

    MODO FACIL
    '''
    def disparar_barco_facil(self, tablero):
        disparos = 1
        while disparos > 0:
            disparos -= 1
            coordenada1 = input("Dame las cordenadas de disparar ")
            x,y=[int(n) for n in coordenada1.split(",")]
            sitio = x,y
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.contador_vidas -= 1
                print("Has disparado a un barco")
                print(f"Te quedan {chequeo_vidas(tablero)}.")
                disparos += 1
            elif tablero.tablero_flota[sitio] == "X":
                print("Intenta en otro sitio")
                disparos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                print("Disparo en agua")

        return tablero.tablero_flota
    
    '''
    DISPARO MANUAL PARA USUARIO, SI HAS DISPARADO ANTES TE VUELVE A PREGUNTAR

    MODO DIFICL
    '''
    def disparar_barco_dificil(self, tablero):
        intentos = 2
        disparos_agua = 0
        while intentos > 0 and disparos_agua < 2:
            intentos -= 1
            coordenada1 = input("Dame las cordenadas de disparar ")
            x,y=[int(n) for n in coordenada1.split(",")]
            sitio = x,y
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.contador_vidas -= 1
                print("Has disparado a un barco")
                print(f"Te quedan {chequeo_vidas(tablero)}.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X":
                print("Intenta en otro sitio")
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                print("Disparo en agua")
                intentos +=1
                disparos_agua += 1
                if disparos_agua == 2:
                    print("has alcanzado el numero maximo de intentos")

        return tablero
