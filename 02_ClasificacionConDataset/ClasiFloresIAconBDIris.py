from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

iris = datasets.load_iris()

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
iris_df["species"] = iris_df['target'].map({0:'setosa', 1:'versicolor', 2:'virginica'})

print("Firs 5 rows of the dataset")
print(iris_df.head(),"\n")

X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}\n")

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, Y_train)

y_pred =modelo.predict(X_test)

result_df = pd.DataFrame({'Actual':Y_test, 'Predicted': y_pred})
result_df['Actual_Species'] = result_df['Actual'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
result_df['Predicted_Species'] = result_df['Predicted'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("Actual vs Predicted Labels:\n", result_df.head(), "\n")

precision = accuracy_score(Y_test, y_pred)
print(f"Model Accuracy: {precision*100:.2f}%")