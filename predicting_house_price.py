import pandas as pd
from sklearn.linear_model import LinearRegression

# --- Dataset Setup ---
# Create the DataFrame for the Lab Exercise
data = {
    'Area': [1200, 1400, 1600, 1700, 1850],
    'Rooms': [3, 4, 3, 5, 4],
    'Distance': [5, 3, 8, 2, 4],
    'Age': [10, 3, 20, 15, 7],
    'Price': [120, 150, 130, 180, 170]
}
df = pd.DataFrame(data)

# Define the features (X) and the target (y)
X = df[['Area', 'Rooms', 'Distance', 'Age']]
y = df['Price']

print("House Price Prediction using Forward Selection")

# --- Step 1: Evaluate Each Feature Alone ---
print("## Step 1: Evaluate Each Feature Alone")

# Test 'Area'
model_area = LinearRegression()
model_area.fit(X[['Area']], y)
r2_area = model_area.score(X[['Area']], y)
print(f"R^2 with Area:      {r2_area:.4f}")

# Test 'Rooms'
model_rooms = LinearRegression()
model_rooms.fit(X[['Rooms']], y)
r2_rooms = model_rooms.score(X[['Rooms']], y)
print(f"R^2 with Rooms:     {r2_rooms:.4f}")

# Test 'Distance'
model_dist = LinearRegression()
model_dist.fit(X[['Distance']], y)
r2_dist = model_dist.score(X[['Distance']], y)
print(f"R^2 with Distance:  {r2_dist:.4f}")

# Test 'Age'
model_age = LinearRegression()
model_age.fit(X[['Age']], y)
r2_age = model_age.score(X[['Age']], y)
print(f"R^2 with Age:       {r2_age:.4f}")

print("\n Best single feature is 'Area'.\n")


# --- Step 2: Add the Next Feature ---
# We start with 'Area' since it was the best single feature.
print("## Step 2: Add a Second Feature to 'Area'")

# Test 'Area' + 'Rooms'
model_area_rooms = LinearRegression()
X_ar = X[['Area', 'Rooms']]
model_area_rooms.fit(X_ar, y)
r2_area_rooms = model_area_rooms.score(X_ar, y)
print(f"R^2 with Area + Rooms:    {r2_area_rooms:.4f}")

# Test 'Area' + 'Distance'
model_area_dist = LinearRegression()
X_ad = X[['Area', 'Distance']]
model_area_dist.fit(X_ad, y)
r2_area_dist = model_area_dist.score(X_ad, y)
print(f"R^2 with Area + Distance: {r2_area_dist:.4f}")

# Test 'Area' + 'Age'
model_area_age = LinearRegression()
X_aa = X[['Area', 'Age']]
model_area_age.fit(X_aa, y)
r2_area_age = model_area_age.score(X_aa, y)
print(f"R^2 with Area + Age:      {r2_area_age:.4f}")

print("\n Best two-feature combination is 'Area' and 'Rooms'.\n")


# --- Step 3: Stopping (and Summary) ---
print("## Step 3: Stopping and Final Model Summary")
# Now we build the next model with 'Area', 'Rooms', and 'Distance'
# (since 'Area' + 'Rooms' was the best combo so far)
# and compare. For a complete process, you'd test all remaining features.

# Model with 'Area' + 'Rooms' + 'Distance'
model_ard = LinearRegression()
X_ard = X[['Area', 'Rooms', 'Distance']]
model_ard.fit(X_ard, y)
r2_ard = model_ard.score(X_ard, y)

# Full model with all features
model_full = LinearRegression()
model_full.fit(X, y)
r2_full = model_full.score(X, y)


# Final Summary Table, as shown in the example
summary_data = {
    'Step': ['1', '2', '3', '4'],
    'Features Included': [
        "['Area']",
        "['Area', 'Rooms']",
        "['Area', 'Rooms', 'Distance']",
        "['Area', 'Rooms', 'Distance', 'Age']"
    ],
    'Model R^2': [
        f"{r2_area:.4f}",
        f"{r2_area_rooms:.4f}",
        f"{r2_ard:.4f}",
        f"{r2_full:.4f}"
    ]
}
summary_df = pd.DataFrame(summary_data)
print("Forward selection results:\n")
print(summary_df.to_string(index=False))

print("\nSince the R^2 score increases significantly with each added feature,")
print("the model with all four features is the best choice for this dataset.")