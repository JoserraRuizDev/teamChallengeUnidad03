#clases
import random
import numpy as np
from variables import *
from funciones import *
class Tablero:
    def __init__(self, nombre_usuario):
        self.id_usuario = nombre_usuario,
        #self.tamano = np.full(10,10)
        self.barcos = flota_barcos
        self.tablero_sin_barcos = np.full((10,10),"O") 
        self.tablero_flota = np.full((10,10),"")  #máquina + nuestros disparos
        self.contador_vidas = 20

    def crear_tablero(relleno = ""):
    # genero tablero
        return np.full((10,10),relleno) 
    
    def posicionar_barco(tablero, coordenada_inicial, coordenada_final, relleno = "O"):
    # posiciono los barcos en el tablero
        fila_inicial = coordenada_inicial[0]
        fila_final = coordenada_final[0]
        columna_inicial = coordenada_inicial[1]
        columna_final = coordenada_final[1]
        if (fila_final < 0
            or fila_final >= tablero.shape[0]
            or columna_final < 0
            or columna_final >= tablero.shape[1]):
            return (tablero, "No se puede posicionar")
        
        tablero_resultante = np.copy(tablero)

        for i in range(fila_inicial,fila_final + 1):
            for j in range(columna_inicial,columna_final + 1):
                if (tablero_resultante[i,j] == relleno):
                    return (tablero, "No se puede posicionar")
                else:
                    tablero_resultante[i,j] = relleno
        return (tablero_resultante, "Posicionado")

    def posicionar_barco_aleatorio(self):
        for barco, eslora in self.barcos[0].items():
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
    
            print("Posicionando en: " + str((fila_inicial, columna_inicial)) + ", " + str((fila_final, columna_final)) + " orientacion " + orientacion)
            return Tablero.posicionar_barco_con_orientacion(self.tablero_flota, (fila_inicial, columna_inicial), (fila_final, columna_final))
    
    def posicionar_barco_con_orientacion(tablero, coordenada_inicial, coordenada_final, relleno = "O"):
    # posiciono los barcos en el tablero en coordenada_inicial y coordenada_final ambas incluídas con orientacion
        fila_inicial = coordenada_inicial[0]
        fila_final = coordenada_final[0]
        columna_inicial = coordenada_inicial[1]
        columna_final = coordenada_final[1]
        # Comprobar que la coordenada inicial entra en el tablero
        if (fila_inicial < 0
            or fila_inicial >= tablero.shape[0]
            or columna_inicial < 0
            or columna_inicial >= tablero.shape[1]):
            return (tablero, "No se puede posicionar: coordenada inicial fuera del tablero")
        
        # Comprobar que la coordenada final entra en el tablero
        if (fila_final < 0
            or fila_final >= tablero.shape[0]
            or columna_final < 0
            or columna_final >= tablero.shape[1]):
            return (tablero, "No se puede posicionar: coordenada final fuera del tablero")

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
        tablero_resultante = np.copy(tablero)
        for i in recorrido_fila:
            for j in recorrido_columna:
                if (tablero_resultante[i,j] == relleno):
                    return (tablero, "No se puede posicionar: Coordenadas ocupadas")
                else:
                    tablero_resultante[i,j] = relleno
        return (tablero_resultante, "Barco posicionado")
    
    """"
    FUNCION DISPARAR DE MODO ALEATORIO:

    NIVEL FACIL

    """

    def dispara_random_facil(self, tablero):
        coor_1 = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
        coor_2 = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
        disparo = (coor_1, coor_2) 
        
        agua = np.array(tablero.tablero_flota[disparo] == "")

        if agua == True:
            tablero.tablero_flota[disparo] = "-"
            print(f"¡Agua! Has disparado a la coordenada {disparo}.")
        else:
            tablero.tablero_flota[disparo] = "X"
            if chequeo_vidas(tablero) == 0:
                return "HAS PERDIDO"
            print(f"¡Tocado! Has acertado disparando a la coordenada{disparo}.")

        return (tablero.tablero_flota, tablero.contador_vidas)
    
    '''
    FUNCION DISPARAR DE MODO ALEATORIO:

    MODO DIFICL ()
    '''

    def dispara_random_difil(self, tablero):
        
        intentos = 0
        while intentos <=2:
            coor_1 = np.random.randint(0,10)   # establecemos  el primer elemento de mi coordenada aleatoria, elemento fila 
            coor_2 = np.random.randint(0,10)   # establecemos el segundo elemento de mi coordenada origen aleatoria, elemento columna
            disparo = (coor_1, coor_2) 
            
            agua = tablero[disparo] == ""
        
            if agua == True:
                tablero[disparo] = "-"
                print(f"¡Agua! Has disparado a la coordenada {disparo}.")
                intentos +=1
                if intentos == 2: #SI LLEGA A DOS INTENTOS SE PARA
                    print("Has alcanzado el número máximo de intentos")
                    break
            elif tablero[disparo] == "O":
                tablero[disparo] = "X"
                print(f"¡Tocado! Has acertado disparando a la coordenada{disparo}.")
                break #SI LE DAMOS AL BARCO SE PARA TMB
                
        return tablero
    
    '''
    DISPARO MANUAL PARA USUARIO, SI HAS DISPARADO ANTES TE VUELVE A PREGUNTAR

    MODO FACIL
    '''
    def disparar_barco_facil(self, tablero):
        while True:
            cordenada1 = input("Dame las cordenadas de disparar ")
            try:
                x,y=[int(n) for n in cordenada1.split(",")]
                sitio = x,y
        
                if tablero[sitio] == "O":
                    tablero[sitio] = "X"
                    print("Has disparado a un barco")
                    break
                elif tablero[sitio] == "X":
                    print("Intenta en otro sitio")
                
                else:
                    tablero[sitio] = "-"
                    print("Disparo en agua")
                    break
            except NameError:
                None

        return tablero
    
    '''
DISPARO MANUAL PARA USUARIO, SI HAS DISPARADO ANTES TE VUELVE A PREGUNTAR

MODO DIFICL
'''
    def disparar_barco_dificil(self, tablero):
        intentos = 0
        while intentos <=2:
            cordenada1 = input("Dame las cordenadas de disparar ")
            try:
                x,y=[int(n) for n in cordenada1.split(",")]
                sitio = x,y
        
                if tablero[sitio] == "O":
                    tablero[sitio] = "X"
                    print("Has disparado a un barco")
                    break
                elif tablero[sitio] == "X":
                    print("Intenta en otro sitio")
                
                else:
                    tablero[sitio] = "-"
                    print("Disparo en agua")
                    intentos +=1
                    if intentos == 2:
                        print("has alcanzado el numero maximo de intentos")
                        break
            except NameError:
                None

        return tablero