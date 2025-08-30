import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Data (y = 7x - 5 with noise)
X = np.linspace(-20, 15, 200)
Y = 7 * X - 5 + np.random.randn(*X.shape) * 3  # Added noise

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mse')

# Train
model.fit(X, Y, epochs=200, verbose=0)

# Extract learned parameters
weights, bias = model.layers[0].get_weights()
slope = weights[0][0]
intercept = bias[0]

print("🔎 Learned Parameters:")
print(f"Slope (weight): {slope:.4f}")
print(f"Intercept (bias): {intercept:.4f}")

# Predict
Y_pred = model.predict(X)

# Plot with labels
plt.scatter(X, Y, color="blue", label="Data")
plt.plot(X, Y_pred, color="red", label=f"Fitted Line (y = {slope:.2f}x + {intercept:.2f})")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression using TensorFlow")
plt.legend()
plt.show()
