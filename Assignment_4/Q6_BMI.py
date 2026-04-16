'''
Program to calculate BMI and health status from CSV file.
'''

import pandas as pd

# Read CSV file
data = pd.read_csv("health_data.csv")

# Calculate BMI
data["BMI"] = data["weight"] / data["height"]

# Create function for health status
def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Healthy"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "High Risk"
    else:
        return "Critical"

# Apply function to all rows
data["Health_Status"] = data["BMI"].apply(get_status)

# Display result
print(data)