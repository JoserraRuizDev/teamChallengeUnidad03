from clases_trabajando2 import *

flota_barcos = {"barco_1.1": 1, #eslora 1
               "barco_1.2": 1, #eslora 1
               "barco_1.3": 1, #eslora 1
               "barco_1.4": 1, #eslora 1
               "barco_2.1": 2, #eslora 2
               "barco_2.2": 2, #eslora 2
               "barco_2.3": 2, #eslora 2
               "barco_3.1": 3, #eslora 3
               "barco_3.2": 3, #eslora 3
               "barco_4.1": 4, #eslora 4
               }

NOMBRE_USUARIO_CPU = "CPU"

REGLAS_DEL_JUEGO = """Reglas del juego:"
"Objetivo del juego
El objetivo es sencillo: hundir todos los barcos del oponente antes de que él hunda los tuyos.

Para lograrlo, necesitas deducir la ubicación de sus barcos y acertar tus disparos en las coordenadas correctas.

Preparación del juego
Cada jugador tiene dos tableros de 10×10 casillas.

Uno se utiliza para colocar tus propios barcos y registrar los impactos recibidos, mientras que el otro sirve para marcar tus disparos y registrar los resultados contra la flota enemiga.

Colocación de los barcos
Cada jugador tiene una flota de diez barcos de diferentes tamaños:

Los barcos se pueden colocar de manera horizontal o vertical, pero nunca en diagonal. No pueden superponerse ni tocarse entre sí.

Desarrollo del juego
Una vez que ambos jugadores han colocado sus barcos, comienza el juego.

Los jugadores se turnan para disparar a coordenadas específicas en el tablero del oponente.

Disparo: El jugador elige una coordenada (por ejemplo, B5). El oponente verifica si esa coordenada contiene parte de un barco.
Resultados del disparo:
Agua: Si no hay ningún barco en esa coordenada, el oponente dice «Agua».
Tocado: Si hay un barco, el oponente dice «Tocado» y el jugador marca la casilla con una 
'X'. 
Turnos: Si el jugador acierta (toca o hunde), puede seguir disparando hasta fallar. Si falla, es el turno del oponente.

Fin del juego
El juego termina cuando uno de los jugadores ha hundido todos los barcos del oponente.

El jugador que lo consiga primero es declarado el ganador."""