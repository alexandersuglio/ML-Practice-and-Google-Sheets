import tensorflow as tf
import numpy as np

# Training data
X = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
Y = np.array([1.0, 3.0, 5.0, 7.0], dtype=np.float32)

# Define the model using Keras
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Fit the model
model.fit(X, Y, epochs=300, verbose=0)

# Print weight and bias
weights = model.get_weights()
print(f"Trained W: {weights[0][0][0]}, b: {weights[1][0]}")

# Trained W: 1.8078786134719849, b: -0.43513986468315125
