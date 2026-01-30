from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

iris = datasets.load_iris()

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("Primeras 5 filas del conjunto de datos")
print(iris_df.head(), "\n")

X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 42)

print(f"Muestras de entrenamiento: {len(X_train)}, Muestras de prueba: {len(X_test)}\n")

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, Y_train)

print("\n Rango de cada caracteristica: ")

for feature, (min_val, max_val) in zip(iris.feature_names, zip(X.min(axis=0), (X.max(axis=0)))):
    print(f"{feature.capitalize()} - Min: {min_val:.2f}, Max: {max_val:.2f}")

print("\n Ingresa las caracteristicas de la flor: \n")
sepal_length = float(input("Largo del sépalo (cm): "))
sepal_width = float(input("Ancho del sépalo (cm): "))
petal_length = float(input("Largo del petalo: (cm): "))
petal_width = float(input("Ancho del petalo: (cm): "))

user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted_species_index = modelo.predict(user_input)[0]
predicted_species = iris.target_names[predicted_species_index]

print(f"\n Especie predicha por la flor: {predicted_species}")