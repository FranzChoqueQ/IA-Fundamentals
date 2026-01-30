from sklearn import datasets
import pandas as pd

#Cargar el conjunto de datos iris
iris = datasets.load_iris()

#Convertir a Dataframe de pandas para mejor visualizacion
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Agregar la columna de l aespecio (0 = setosa, 1 = versicolor, 2 = virginica)
df["species"] = iris.target

#Imprimir todas las filas
print(df.to_string())

