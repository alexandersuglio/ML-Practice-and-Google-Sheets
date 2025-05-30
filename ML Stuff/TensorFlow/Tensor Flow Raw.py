import tensorflow as tf
import numpy as np

# Training data
X = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
Y = np.array([1.0, 3.0, 5.0, 7.0], dtype=np.float32)

# Initialize parameters: weight and bias
W = tf.Variable(0.0)  # model's slope
b = tf.Variable(0.0)  # model's intercept

def model(x):
    return W * x + b  # This is your hypothesis: ŷ = Wx + b

def loss_fn(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))  # MSE

optimizer = tf.optimizers.SGD(learning_rate=0.01)

for epoch in range(300):
    with tf.GradientTape() as tape:
        y_pred = model(X)              # Forward pass
        loss = loss_fn(Y, y_pred)      # Compute loss
    gradients = tape.gradient(loss, [W, b])  # Backpropagation
    optimizer.apply_gradients(zip(gradients, [W, b]))  # Gradient descent step

print(f"Trained W: {W.numpy()}, b: {b.numpy()}")
