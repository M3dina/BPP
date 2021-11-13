import pandas as pd
import matplotlib.pyplot as plt


class GastoIngreso:
    """
        Clase GastoIngreso
            mes = indica el mes del gasto o ingreso
            valor = indica el valor de ese gasto o ingreso
    """
    def __init__(self, mes, valor):
        self.mes = mes
        self.valor = valor


def leerFichero(path):
    """
        Metodo leerFichero. Abre y lee el fichero facilitado en el path para convertirlo en un DataFrame 'pandas'.

        Input:
            path -> ruta donde se encuentra el fichero (si es nula, se pondrá por defecto 'finanzas2020.csv').
        Output:
            df -> DataFrame del fichero facilitado por el path o del fichero por defecto 'finanzas2020.csv'
        Excepciones:
            FileNotFoundError -> excepción para controlar si no se encuentra el fichero
    """
    try:
        if path is None:
            df = pd.read_csv('finanzas2020.csv', delim_whitespace=True, decimal=",", thousands=".")
            return df
        else:
            df = pd.read_csv(path, delim_whitespace=True, decimal=",", thousands=".")
            return df
    except FileNotFoundError:
        print("El fichero no se encuentra en la ruta descrita o no se ha declarado el nombre correcto.")
        return 0


def comprobarFichero(df):
    """
        Metodo comprobarFichero. Comprueba que el DataFrame facilitado contiene 12 columnas.

        Input:
            df -> DataFrame de pandas.
        Output:
            Nada
        Excepciones:
            IndexError -> excepción para controlar si no se encuentra un valor en el índice definido.
    """
    columnas = 12
    try:
        df.columns.values[columnas-1]
    except IndexError:
        print("El fichero facilitado no contiene 12 columnas, por lo que no tiene valores para todos los meses.")


def leerDatos(df):
    """
        Metodo leerDatos. Lee los datos de un Dataframe por columnas y por filas. Una vez se lean los datos, se creará un diccionario
                    relacionando las columnas con los valores totales de sus filas según sean ingresos (positivo) y gastos (negativo).

        Input:
            df -> DataFrame de pandas.
        Output:
            gastos -> Diccionario (mes, valor) de los gastos
            ingresos -> Diccionario (mes, valor) de los ingresos
            incorrect_values -> Cuenta de los valores incorrectos detectados en el DataFrame
        Excepciones:
            IndexError -> excepción para controlar si no se encuentra un valor en el índice definido.
            TypeError -> excepción para controlar si el tipo de datos no es correcto.
            ValueError -> excepción para controlar si el valor no es correcto.
    """
    gastos = {}
    ingresos = {}
    resultado = 0
    ahorro = 0
    columnsNames = df.columns.values
    incorrect_values = 0
    try:
        for name in columnsNames:
            for i in range(0, 11):
                filas = len(df.index)
                for j in range(0, filas):
                    try:
                        if df[name][j] < 0:
                            resultado += df[name][j]
                        else:
                            ahorro += df[name][j]
                    except TypeError:
                        try:
                            if int(df[name][j].replace("'", "")) < 0:
                                resultado += int(df[name][j].replace("'", ""))
                            else:
                                ahorro += int(df[name][j].replace("'", ""))
                        except ValueError:
                            incorrect_values += 1
            gastos[name] = resultado
            ingresos[name] = ahorro
        return gastos, ingresos, incorrect_values
    except IndexError:
        print("El fichero facilitado no contiene valores para una de las columnas facilitadas")


def obtenerMax(gastos):
    """
        Metodo obtenerMax. Calcula el máximo valor de ingreso/gasto de un diccionario facilitado, pasado por parámetro.

        Input:
            ingresos_gastos -> Diccionario (mes, valor).
        Output:
            GastoIngreso -> Objeto GastoIngreso con los respectivos datos (mes, valor)
    """
    mes_max_gastos = ''
    valor_max_gastos = 0
    for clave in gastos:
        if abs(gastos[clave]) > valor_max_gastos:
            valor_max_gastos = gastos[clave]
            mes_max_gastos = clave
    return GastoIngreso(mes_max_gastos, valor_max_gastos)


def media(lista):
    """
        Metodo media. Calcula la media de una lista de valores facilitados.

        Input:
            lista -> diccionario de valores.
        Output:
            media -> valor de la media de la lista de valores
    """
    sumaTotal = 0
    for clave in lista:
        sumaTotal += lista[clave]
    return sumaTotal/len(lista)


def total(lista):
    """
        Metodo total. Calcula el total de una lista de valores facilitados.

        Input:
            lista -> diccionario de valores.
        Output:
            sumaTotal -> valor de la suma de la lista de valores
    """
    sumaTotal = 0
    for clave in lista:
        sumaTotal += lista[clave]
    return sumaTotal


def grafico(valores):
    """
        Metodo grafico. Crea el grafico de una lista de valores facilitados.

        Input:
            lista -> diccionario de valores.
        Output:
            plt.show() -> muestra el grafico creado.
    """
    names = []
    values = []
    for clave in valores:
        names.append(clave)
        values.append(valores[clave])
    plt.figure(figsize=(9, 6))
    plt.bar(names, values)
    plt.show()

'''
def init():
    print("Comenzamos con la realización de las tareas de la práctica 1:")
    print("\n")
    # Comprobamos si existe el fichero y lo convertimos en un Dataframe
    df = leerFichero(None)
    # Comprobamos que el Dataframe contiene 12 columnas
    comprobarFichero(df)
    # Variable que contendrá el total de valores incorrectos del csv facilitado
    incorrect_values = 0
    # Leemos los datos del ficheros, separándolos entre gastos e ingresos
    gastos, ingresos, incorrect_values = leerDatos(df)
    # Obtenemos el mes que más gastos ha habido y el valor
    final_gastos = obtenerMax(gastos)
    # Obtenemos el mes que más ingresos ha habido y el valor
    final_ingresos = obtenerMax(ingresos)
    # Presentamos las respuestas a las tareas solicitadas en la práctica
    print(f'¿Qué mes se ha gastado más? El mes es {final_gastos.mes} con un valor de: {final_gastos.valor}')
    print(f'¿Qué mes se ha ahorrado más? El mes es {final_ingresos.mes} con un valor de: {final_ingresos.valor}')
    print(f'¿Cuál es la media de gastos al año? La media ha sido {media(gastos)} ({abs(media(gastos))})')
    print(f'¿Cuál ha sido el gasto total a lo largo del año? El total de gastos ha sido {total(gastos)}')
    print(f'¿Cuáles han sido los ingresos totales a lo largo del año? El total de ingresos ha sido {total(ingresos)}')
    print("El gráfico de la evolución de ingresos a lo largo del año:")
    grafico(ingresos)
    resultado = input("¿Quieres calcular la gráfica de gastos a lo largo del año? (Si/No)")
    if resultado == 'Si':
        grafico(gastos)
    else:
        print("Ha decidido no presentar la gráfica de gastos a lo largo del año")
    print(f'El número total de valores incorrectos en el csv es:{incorrect_values}')


init()
'''
