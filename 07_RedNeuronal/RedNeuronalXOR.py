import tensorflow as tf
import numpy as np

# Corregir la definición de X e y con paréntesis adicionales para el array
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, input_dim=2, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=1000, verbose=0)

loss, accuracy = model.evaluate(X, y)
print("Loss: ", loss)
print("Accuracy: ", accuracy)

predictions = model.predict(X)
print("Predictions:")
for i in range(0,4):
    print(X[i], predictions[i])
