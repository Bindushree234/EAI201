import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# --- User input for line equation ---
slope = float(input("Enter the slope value: "))
intercept = float(input("Enter the intercept value: "))

# --- Generate synthetic data ---
x_vals = np.linspace(5, 15, 80)
noise = np.random.normal(0, 1.2, size=x_vals.shape)
y_vals = slope * x_vals + intercept + noise

# --- Define regression model ---
regressor = tf.keras.Sequential()
regressor.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))

# --- Compile with Adam optimizer ---
regressor.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
                  loss="mse")

# --- Train the model ---
print("Model is training, please wait...")
history = regressor.fit(x_vals, y_vals, epochs=100, verbose=0)
print("Training finished!")

# --- Extract weights ---
learned_w, learned_b = regressor.layers[0].get_weights()
print(f"Equation learned: y = {learned_w[0][0]:.2f}x + {learned_b[0]:.2f}")

# --- Visualization ---
plt.figure(figsize=(8, 5))
plt.scatter(x_vals, y_vals, alpha=0.7, label="Observed data")
pred_y = regressor.predict(x_vals.reshape(-1, 1))
plt.plot(x_vals, pred_y, color="orange", linewidth=2, label="Regression line")
plt.title("Linear Regression using TensorFlow")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
