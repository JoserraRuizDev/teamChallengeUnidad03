#clases
import random
import numpy as np
from variables import *
class Tablero:
    def __init__(self, nombre_usuario, tamano,flota_barcos,tablero_sin_barcos,tablero):
        self.id_usuario = nombre_usuario, 
        self.tamano = tamano
        self.barcos = flota_barcos,
        self.tablero_sin_barcos = tablero_sin_barcos
        self.tablero = tablero #máquina + nuestros disparos

    def posicionar_barco_aleatorio(flota_barcos):
        for barco, eslora in flota_barcos.items():
    # Generar coordenada inicial aleatoria randint(0, 9)
            fila_inicial = random.randint(0, tablero.shape[0] - 1)
            columna_inicial = random.randint(0, tablero.shape[1] - 1)
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
            return Tablero.posicionar_barco_con_orientacion(tablero, (fila_inicial, columna_inicial), (fila_final, columna_final))
    
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