import pandas as pd

# Read the original CSV file
original_df = pd.read_csv("fuel.csv", low_memory=False)

# Select the first 100 rows and first 10 columns
selected_data = original_df.iloc[:100, :10]

# Write the selected data to a new CSV file
selected_data.to_csv("selected_fuel_data.csv", index=False)

print("Data copied successfully!")
