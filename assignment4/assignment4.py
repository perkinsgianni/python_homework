# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

import json
import pandas as pd
import numpy as np

# define data dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# df = pd.DataFrame(data)
# print(f"Original dataframe:\n {df}")

# convert dict to df, assign df to var
task1_data_frame = pd.DataFrame(data)
print(f"Original dataframe:\n {task1_data_frame}")

# create copy, insert salary column & values
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(f"New salary column:\n {task1_with_salary}")

# create copy, increment ages column by 1
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(f"Incremented ages:\n {task1_older}")

# save df to csv file
task1_older.to_csv("employees.csv", index=False)

#//////////////////////////////////////

# Task 2: Loading Data from CSV and JSON

# load csv file, assign to var
task2_employees = pd.read_csv('employees.csv')
print(f"Task 2 dataframe:\n {task2_employees}")

# create list of dicts for add'l employees
additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]
# print(f"Add'l employees:\n {additional_employees}")

# convert list to json str
additional_employees_json = json.dumps(additional_employees)

# create json file, write contents
with open("./additional_employees.json", "w") as file:
    file.write(additional_employees_json)

# load json file, assign to var
json_employees = pd.read_json('additional_employees.json')
print(f"Add'l employees dataframe:\n {json_employees}")

# concat dfs
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(f"Combined dataframes:\n {more_employees}")

#//////////////////////////////////////

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# inspect first 3 rows
first_three = more_employees.head(3)
print(f"First three rows of employees:\n {first_three}")

# inspect last two rows
last_two = more_employees.tail(2)
print(f"Last two rows of employees:\n {last_two}")

# inspect dimensions (num of rows, columns)
# shape is an attribute
employee_shape = more_employees.shape
print(f"Dimensions: {employee_shape}")

# get df summary
more_employees.info()

#//////////////////////////////////////

# Task 4: Data Cleaning

# load csv file, assign to var
dirty_data = pd.read_csv('dirty_data.csv')
print(f"Dirty data:\n {dirty_data}")

# create copy
clean_data = dirty_data.copy()
print(f"Clean data:\n {clean_data}")

# remove dupes
clean_data = clean_data.drop_duplicates()
print(f"Duplicates removed:\n {clean_data}")

# convert ages to numeric
# "coerce" replaces placeholders with NaN
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")
print(f"Numeric ages:\n {clean_data}")

# replace unknown, n/a with NaN
clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a"],
    np.nan
)

# convert salaries to numeric
# "coerce" replaces placeholders with NaN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")
print(f"Numeric salaries:\n {clean_data}")

# fill NaN values with mean ages, median salaries
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(f"Mean ages, median salaries:\n {clean_data}")

# convert hire date to datetime
# "coerce" replaces placeholders with NaT, format="mixed" allows multiple formats
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce", format="mixed")

# fill NaT with timestamp (pd equivalent of python’s datetime) to enforce datetime type
# clean_data['Hire Date'] = clean_data['Hire Date'].fillna(pd.Timestamp('2023-01-01'))
print(f"Converted hire dates:\n {clean_data}")

# strip whitespace, standardize name & dept as uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(f"Uppercase standardization:\n {clean_data}")