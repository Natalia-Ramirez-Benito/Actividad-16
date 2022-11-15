import pandas as pd
import matplotlib.pyplot as plt

# consume los datos del archivo suelo


def consumirsuelo():
    datos = pd.read_csv('suelo.csv')
    print(datos)


consumirsuelo()
# almacena en un dataFrame el NO:ENS, la superficie y el TIPUSSOL


def almacenadf():
    datos = pd.read_csv('suelo.csv')
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    df.SUPERFICIE.plot.hist()


almacenadf()
# gráfico de dispersión de los totales de superficie por TIPUSSOL


def consumirdispersion():
    datos = pd.read_csv('suelo.csv')
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL', 'CODI_TIPUSSOL']]
    df.plot.scatter(x='CODI_TIPUSSOL', y='SUPERFICIE', alpha=0.8)
    plt.show()


consumirdispersion()
#gráfico de barras de la superficie media de los 10 primeros NOM_ENS


def consumirbarras():
    datos = pd.read_csv('suelo.csv')
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    superficie_media = df.groupby("NOM_ENS")["SUPERFICE"].mean()
    superficie_media.head(10).plot.barh()
    plt.show()


consumirbarras()
# gráficos circular de las superficies de 10 títulos


def consumircircular():
    datos = pd.read_csv('suelo.csv')
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    df.SUPERFICIE.head(10).plot.pie()
    plt.show()


consumircircular()