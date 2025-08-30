import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# slope and intercept
slope = 3.0
intercept = 2.0

X = np.linspace(-10, 10, 100)  # input values
y = slope * X + intercept 

# Create a linear regression model: y = wx + b
model = tf.keras.Sequential([ tf.keras.layers.Dense(units=1, input_shape=[1])])

# Compile model 
model.compile(optimizer='sgd', loss='mse')

# Train model 
history = model.fit(X, y, epochs=200, verbose=0)

# Extract learned slope and intercept
weights = model.layers[0].get_weights()
m = weights[0][0][0]  
c = weights[1][0]     

print(f"Learned slope (m): {m:.2f}, Learned intercept (c): {c:.2f}")

# Predictions
y_pred = model.predict(X)

# Plot data vs learned line
plt.scatter(X, y, label="Data")
plt.plot(X, y_pred, color="red", label="Learned Line")
plt.legend()
plt.show()
