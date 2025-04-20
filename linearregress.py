import numpy as np

# Data: Advertising Budget (X) and Sales (Y)
X = np.array([2, 3, 5, 7, 8])  # Advertising Budget (in thousands of dollars)
Y = np.array([4, 5, 7, 10, 11])  # Sales (in thousands of units)

# Calculate the mean of X and Y
X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Calculate the slope (b1) and intercept (b0)
b1 = np.sum((X - X_mean) * (Y - Y_mean)) / np.sum((X - X_mean) ** 2)
b0 = Y_mean - b1 * X_mean

# Print the slope and intercept
print("Intercept (b0):", b0)
print("Slope (b1):", b1)

# Prediction function
def predict(advertising_budget):
    return b0 + b1 * advertising_budget

# Example prediction
advertising_budget = 6  # Example advertising budget in thousands of dollars
predicted_sales = predict(advertising_budget)
print(f"Predicted sales for an advertising budget of ${advertising_budget}k: {predicted_sales:.2f}k units")
