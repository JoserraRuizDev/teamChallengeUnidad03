from clases_trabajando import Tablero

def test_init():
    result = Tablero(nombre_usuario="::test::")

    assert result.id_usuario == "::test::"
    assert result.contador_vidas == 20
    assert result.tablero_sin_barcos.shape == (10, 10)
    assert (result.tablero_sin_barcos == " ").all()
    assert result.tablero_flota.shape == (10, 10)
    assert (result.tablero_flota == " ").all()
    assert result.barcos != None

def test_crear_tablero():
    result = Tablero.crear_tablero()

    assert result.shape == (10, 10)
    assert (result == " ").all()

def test_crear_tablero_con_relleno():
    result = Tablero.crear_tablero(relleno="::relleno::")

    assert result.shape == (10, 10)
    assert (result == "::relleno::").all()

def test_posicionar_barco_con_orientacion():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada = (0,0)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada, coordenada)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[coordenada[0]][coordenada[1]] == "O"

def test_posicionar_barco_con_orientacion():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada = (0,0)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada, coordenada)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[coordenada[0]][coordenada[1]] == "O"

def test_posicionar_barco_con_orientacion_norte():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada_inicial = (5,5)
    coordenada_final = (1,5)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada_inicial, coordenada_final)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[0][5] == " "
    assert tablero_resultado[1][5] == "O"
    assert tablero_resultado[2][5] == "O"
    assert tablero_resultado[3][5] == "O"
    assert tablero_resultado[4][5] == "O"
    assert tablero_resultado[5][5] == "O"
    assert tablero_resultado[6][5] == " "

def test_posicionar_barco_con_orientacion_sur():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada_inicial = (5,5)
    coordenada_final = (9,5)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada_inicial, coordenada_final)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[4][5] == " "
    assert tablero_resultado[5][5] == "O"
    assert tablero_resultado[6][5] == "O"
    assert tablero_resultado[7][5] == "O"
    assert tablero_resultado[8][5] == "O"
    assert tablero_resultado[9][5] == "O"

def test_posicionar_barco_con_orientacion_este():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada_inicial = (5,5)
    coordenada_final = (5,9)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada_inicial, coordenada_final)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[5][4] == " "
    assert tablero_resultado[5][5] == "O"
    assert tablero_resultado[5][6] == "O"
    assert tablero_resultado[5][7] == "O"
    assert tablero_resultado[5][8] == "O"
    assert tablero_resultado[5][9] == "O"

def test_posicionar_barco_con_orientacion_oeste():
    tablero = Tablero(nombre_usuario="::test::")
    coordenada_inicial = (5,5)
    coordenada_final = (5,1)

    tablero_resultado, mensaje_resultado = tablero.posicionar_barco_con_orientacion(coordenada_inicial, coordenada_final)

    assert mensaje_resultado == "Barco posicionado"
    assert (tablero_resultado == tablero.tablero_flota).all()
    assert tablero_resultado[5][0] == " "
    assert tablero_resultado[5][1] == "O"
    assert tablero_resultado[5][2] == "O"
    assert tablero_resultado[5][3] == "O"
    assert tablero_resultado[5][4] == "O"
    assert tablero_resultado[5][5] == "O"
    assert tablero_resultado[5][6] == " "
