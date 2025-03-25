#clases
import random
import numpy as np
from variables import *
from funciones import *

class Tablero:
    def __init__(self, nombre_usuario):
        self.id_usuario = nombre_usuario
        self.barcos = flota_barcos
        self.tablero_sin_barcos = Tablero.crear_tablero() # tablero sin los barcos
        self.tablero_flota = Tablero.crear_tablero() # tablero con la flota de barcos señalada
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
                #print(resultado)
                posicionado = resultado == "Barco posicionado"
        print(f"Flota {self.id_usuario} posicionada")
            
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
        while intentos > 0 and tablero.contador_vidas > 0:
            intentos -= 1
            fila = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
            columna = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
            sitio = (fila, columna)
            coordenadas = (fila+1, columna+1)
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.tablero_sin_barcos[sitio] = "X"
                tablero.contador_vidas -= 1
                print(f"¡TOCADO! Has acertado disparando a la coordenada {coordenadas}.")
                print(f"Vidas restantes de tu oponente: {tablero.contador_vidas}.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X" or tablero.tablero_flota[sitio] == "-":
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                tablero.tablero_sin_barcos[sitio] = "-"
                print(f"¡AGUA! Has fallado disparando a la coordenada {coordenadas}.")

    '''
    FUNCION DISPARAR DE MODO ALEATORIO:

    MODO DIFICL ()
    '''

    def dispara_random_dificil(self, tablero):
        intentos = 2
        disparos_agua = 0
        while intentos > 0 and disparos_agua < 2:
            intentos -= 1
            fila = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
            columna = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
            sitio = (fila, columna)
            coordenadas = (fila+1, columna+1)
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.tablero_sin_barcos[sitio] = "X"
                tablero.contador_vidas -= 1
                print(f"¡TOCADO! Has acertado disparando a la coordenada {coordenadas}.")
                print(f"Vidas restantes de tu oponente: {tablero.contador_vidas}.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X" or tablero.tablero_flota[sitio] == "-":
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                tablero.tablero_flota[sitio] = "-"
                print(f"¡AGUA! Has fallado disparando a la coordenada {coordenadas}.")
                intentos +=1
                disparos_agua += 1
                if disparos_agua == 2:
                    print("¡PIERDES TURNO! Has alcanzado el máximo de intentos.")   
                    break           
    
    '''
    DISPARO MANUAL PARA USUARIO, SI HAS DISPARADO ANTES TE VUELVE A PREGUNTAR

    MODO FACIL
    '''
    def dispara_manual(self, tablero):
        intentos = 1
        while intentos > 0 and tablero.contador_vidas > 0:
            intentos -= 1

            while True:
                coordenada = input("Introduce las coordenadas de tu disparo, ejemplo: 5,9\n")
                                                                                 
                sitio = self.comprobar_coordenadas(coordenada) 
                if sitio is not False:                                        # Basicamente si la funcion de abajo no devuelve False, deja de preguntar las coordenadas
                    break    
            
            if tablero.tablero_flota[sitio] == "O":
                tablero.tablero_flota[sitio] = "X"
                tablero.tablero_sin_barcos[sitio] = "X"
                tablero.contador_vidas -= 1
                print(f"¡TOCADO! Has acertado disparando a la coordenada ({coordenada}).")
                print(tablero.tablero_sin_barcos)
                print(f"Vidas restantes de tu oponente: {tablero.contador_vidas}.")
                intentos += 1
            elif tablero.tablero_flota[sitio] == "X" or tablero.tablero_flota[sitio] == "-":
                print("Ya has disparado en esta coordenada, dispara de nuevo.")
                intentos += 1
            else:
                tablero.tablero_flota[sitio] = "-"
                tablero.tablero_sin_barcos[sitio] = "-"
                print(f"¡AGUA! Has fallado disparando a la coordenada ({coordenada}).")
                break
        return (tablero.tablero_sin_barcos, tablero.contador_vidas)
    

    def comprobar_coordenadas(self, coordenadas):

        if "ABANDONAR" == coordenadas.upper():
            abandonar_partida(self)
        
        try:
            x,y=[int(n) for n in coordenadas.split(",")]
            if x >=1 and x <=10 and y >=1 and y <=10:                           #Tiene que detectar que es un numero entre 1 y 10
                return x-1,y-1
            else:
                print('Las coordenadas tiene que ser entre 1 y 10, ambos incluidos')
                return False
        except ValueError:
            print('Las coordenadas están formadas de numeros, separados por una coma, ejemplo: 7,8')
            return False