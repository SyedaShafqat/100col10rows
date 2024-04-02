
## Add CSV Data
To start the analysis, we need some data. Let's add a CSV file named `fuel.csv` containing our dataset.
## Number of Rows and Columns in Original Data
- Number of rows: 38114
- Number of columns: 81

![Data Screenshot](https://github.com/SyedaShafqat/100col10rows/blob/master/data.png)

## Selected Data
- Number of rows: 10
- Number of columns: 100
- The below script outlines the process of selecting a subset of data from an original CSV file, saving it to a new CSV file.

## Python Script
```python
import pandas as pd

# Read the original CSV file
original_df = pd.read_csv("fuel.csv")

# Select 100 columns and 10 rows
selected_data = original_df.iloc[:10, :100]

# Write the selected data to a new CSV file
selected_data.to_csv("selected_data.csv", index=False)
```
![Data Screenshot](https://github.com/SyedaShafqat/100col10rows/blob/master/fuel2.png)
# Display the rows and columns of the new CSV file
![Data Screenshot](https://github.com/SyedaShafqat/100col10rows/blob/master/fuel4.png)

# Display the contents of the new CSV file containg 100 rows and 10 columns
```
print("Selected data:")
print(selected_data)
```
![Data Screenshot](https://github.com/SyedaShafqat/100col10rows/blob/master/FUEL5.png)
