import pandas as pd
import matplotlib.pyplot as plt


def consumirHistograma():
    datos = pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[["RM", "CRIM", "TOWN", "TAX"]] #convertir los datos en DataFrame
    #print(df)
    df.CRIM.plot.hist()
    plt.show()

#consumirHistograma()


def consumirDispersion():
    datos = pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    df.plot.scatter(x='CRIM', y='MEDV', alpha=0.8)
    plt.show()

#consumirDispersion()


def consumirBarras():
    datos = pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    valor_por_ciudad = df.groupby("TOWN")["MEDV"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()

#consumirBarras()


def consumirCajas():
    datos = pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    #df["VALOR CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.boxplot(column="CRIM", by="MEDV", figdize=(8, 6))
    plt.show()
