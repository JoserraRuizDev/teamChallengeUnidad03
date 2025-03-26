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

#REGLAS_DEL_JUEGO = 
"""Reglas del juego:"
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

El jugador que lo consiga primero es declarado el ganador.

Si deseas abandonar la partida en algún momento, introduce ABANDONAR cuando el juego te pida las coordenadas. ¡CUIDADO! El progreso no se queda guardado.
"""

REGLAS_DEL_JUEGO = '''

==================================================
|           🔹  REGLAS DEL JUEGO  🔹             |
================================================== 

📌 Objetivo del juego
----------------------
El objetivo es sencillo: hundir todos los barcos del oponente antes de que él hunda los tuyos.  
Para lograrlo, necesitas deducir la ubicación de sus barcos y acertar tus disparos en las coordenadas correctas.  

---

📌 PREPARACIÓN DEL JUEGO
------------------------- 
- Cada jugador tiene dos tableros de 10×10 casillas:  
- Uno para colocar tus barcos y registrar los impactos recibidos.  
- Otro para marcar tus disparos y registrar los resultados contra la flota enemiga.  

---

📌 COLOCACIÓN DE LOS BARCOS
----------------------------
- Cada jugador tiene una flota de diez barcos de diferentes tamaños.  
- Los barcos pueden colocarse en posición horizontal o vertical.  
- No pueden colocarse en diagonal, superponerse ni tocarse entre sí.  

---

📌 DESARROLLO DEL JUEGO
------------------------  
- Una vez colocados los barcos, comienza la batalla.  

·Turnos de disparo
- Los jugadores se turnan para disparar a coordenadas en el tablero del oponente.  
- Ejemplo: Si el jugador elige B5, el oponente verifica si hay un barco en esa coordenada.  

·Resultados del disparo  
- Agua -> No hay ningún barco en esa coordenada.  
- Tocado -> Hay un barco en esa coordenada. Se marca con una "X".  
- Hundido -> Si todas las partes de un barco han sido alcanzadas, se hunde.  

·Reglas de turnos  
- Si el jugador acierta (toca o hunde un barco), puede seguir disparando.  
- Si falla, el turno pasa al oponente.  

---

📌 FIN DEL JUEGO
-----------------
- El juego termina cuando uno de los jugadores ha hundido toda la flota enemiga.  
- El primer jugador en lograrlo será el GANADOR.  

---

📌 ABANDONAR
-------------
- Si deseas abandonar la partida en cualquier momento, introduce ABANDONAR cuando el juego te pida las coordenadas.  
- ¡CUIDADO! El progreso no se guarda.

'''