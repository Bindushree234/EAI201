# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

sns.set_style('whitegrid')

print("Step 1: Load Data")

# Load Boston dataset
boston = fetch_openml(name='boston', version=1, as_frame=True)
data = boston.data.copy()

# Convert all features and target to numeric
data = data.apply(pd.to_numeric, errors='coerce')
data['PRICE'] = pd.to_numeric(boston.target, errors='coerce')

# Drop any rows with missing values
data = data.dropna()

print(f"Houses: {data.shape[0]}, Features: {data.shape[1]-1}")
print("\nFirst 5 rows:")
print(data.head())

# Price summary
price = data['PRICE']
print("\nHouse Price Summary:")
print(f"Min: ${price.min()*1000:,.2f}")
print(f"Max: ${price.max()*1000:,.2f}")
print(f"Mean: ${price.mean()*1000:,.2f}")

print("\nStep 2: Explore Data")

# Price distribution
plt.figure(figsize=(10,6))
sns.histplot(price, bins=30, kde=True, color='skyblue')
plt.title("House Price Distribution")
plt.xlabel("Price ($1000s)")
plt.ylabel("Count")
plt.show()

# Feature correlation
corr = data.corr()['PRICE'].sort_values(ascending=False)
print("\nFeature Correlation with Price:")
print(corr)

# Top correlated feature scatter plot
top_feature = corr.index[1]
print(f"\nMost correlated feature: {top_feature}")

plt.figure(figsize=(10,6))
sns.scatterplot(x=data[top_feature], y=price, color='green')
plt.title(f"Price vs {top_feature}")
plt.xlabel(top_feature)
plt.ylabel("Price ($1000s)")
plt.show()

print("Observation: Price distribution is right-skewed. Most houses are mid-priced, few are expensive.")

print("\nStep 3: Train Model")

# Prepare data
X = data.drop(columns='PRICE')
y = price

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained successfully!")

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Performance:")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f} ($1000s)")

# Actual vs Predicted plot
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.6, color='purple')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title("Actual vs Predicted Prices")
plt.xlabel("Actual Prices ($1000s)")
plt.ylabel("Predicted Prices ($1000s)")
plt.show()

print("\nStep 4: Analysis")
print(f"R² score: {r2:.4f} → Model explains about {r2:.1%} of variance.")
print("Model predicts mid-range houses well, but underestimates very expensive ones.")
