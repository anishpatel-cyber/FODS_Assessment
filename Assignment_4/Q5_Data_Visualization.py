'''
Program to read CSV file "health_data.csv" using pandas and plot the data using
Matplotlib.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("health_data.csv")

# Scatter plots
# Plots 1
plt.scatter(data["weight"], data["height"])
plt.title("Weight vs Height")
plt.show()

# Plots 2
plt.scatter(data["age"], data["weight"])
plt.title("Age vs Weight")
plt.show()

# Plots 3
plt.scatter(data["height"], data["age"])
plt.title("height vs age")
plt.show()

# Plots 4
plt.scatter(data["gender"], data["height"])
plt.title("Gender vs Height")
plt.show()

# Plots 5
plt.scatter(data["gender"], data["weight"])
plt.title("Gender vs Weight")
plt.show()