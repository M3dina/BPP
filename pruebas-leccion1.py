import pytest
import leccion1


def test_media():
    diccionario = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    valor_incorrecto = 10
    valor_test = leccion1.media(diccionario)
    valor_correcto = 3
    assert valor_test == valor_correcto
    assert valor_test != valor_incorrecto


def test_maximo():
    diccionario = {'Enero': 54.5, 'Febrero': 70.2, 'Marzo': 103.2, 'Abril': 103.3}
    valor_incorrecto_mes = 'Enero'
    valor_incorrecto_valor = 103.2
    valor_maximo = 103.3
    mes_maximo = ''
    for key, value in diccionario.items():
        if value == valor_maximo:
            mes_maximo = key
    valor_test = leccion1.obtenerMax(diccionario)
    assert valor_test.mes == mes_maximo
    assert valor_test.mes != valor_incorrecto_mes
    assert valor_test.valor == valor_maximo
    assert valor_test.valor != valor_incorrecto_valor


def test_total():
    diccionario = {'Enero': 54.5, 'Febrero': 70.2, 'Marzo': 103.2, 'Abril': 103.3}
    valor_incorrecto_total = 276.7
    valor_correcto = 331.2
    valor_test = leccion1.total(diccionario)
    assert valor_test == valor_correcto
    assert valor_test != valor_incorrecto_total


def test_leerFichero():
    path_erroneo = 'ficheros/finanzas2020.csv'
    valor_erroneo = leccion1.leerFichero(path_erroneo)
    valor_test = leccion1.leerFichero(None)
    valor_filas_correcto = 100
    valor_filas_test = len(valor_test.index)
    assert valor_filas_test == valor_filas_correcto
    assert valor_erroneo == 0
