import numpy as np
import pdb


def es_primo(n):
    """
        Método es_primo, realiza la comprobación de que el entero facilitado por parámetro es primo.
        Parámetros:
            n -> entero
    """
    primo = True
    for i in range(2, n):
        if(n % i == 0):
            primo = False
    return primo


def maxList(listas):
    """
        Método maxList, que dado una lista de listas de n números devuelva el máximo valor de cada una de las listas.
        Parámetros:
            listas -> lista de listas de enteros
    """
    maxValueList = [j for i, j in enumerate(listas) if j == np.max(listas)]
    print(f'Los máximos de cada una de las listas pasadas por parámetro son: {maxValueList}')


def filterPrimo(lista):
    """
        Método filterPrimo, que dado una lista de n números devuelva aquellos que son primos.
        Parámetros:
            lista -> lista de enteros
    """
    primos = list(filter(es_primo, lista))
    print(f'Estos son los primos encontrados en la lista pasada por parámetro: {primos}')


def init():
    """
        Método init(), es la función principal de la clase dónde se definirán
                       las variables locales para llamar al resto de funciones
                       definidas, maxList() y filterPrimo().
    """
    pdb.set_trace()
    # Variables locales
    # Lista de listas para llamar a maxList()
    listas = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    # Lista de números para llamar a filterPrimo()
    listaPrimos = [3, 4, 8, 5, 5, 22, 13]
    # Llamada a los métodos definidos
    maxList(listas)
    filterPrimo(listaPrimos)


# Método principal de la clase, que llamará al método init()
# dónde se realizarán las llamadas a los métodos definidos
if __name__ == '__main__':
    init()
