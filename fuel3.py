import csv

# Function to count the number of rows and columns in a CSV file
def count_rows_and_columns(file_name):
    num_rows = 0
    num_columns = 0
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            num_rows += 1
            if i == 0:  # Check only the first row to get the number of columns
                num_columns = len(row)
    return num_rows, num_columns

# Replace 'new_mvc.csv' with the actual filename of your CSV file
num_rows, num_columns = count_rows_and_columns('selected_fuel_data.csv')

print("Number of rows:", num_rows)
print("Number of columns:", num_columns)
