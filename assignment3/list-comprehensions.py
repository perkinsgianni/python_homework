# Task 3: List Comprehensions Practice

import csv

def read_employees():
    # initialize empty list for employees
    employees_list = []

    with open('../csv/employees.csv', 'r') as file:
        # read content into list of lists
        employees_list = list(csv.reader(file))
        # print(employees_list)

    # skip header row, create list of employee names from each row
    employee_names = [f"{row[1]} {row[2]}" for row in employees_list[1:]]
    print(f"Employee names: {employee_names}")

    # create list of employees names that contain letter “e”
    names_with_e = [name for name in employee_names if "e" in name.lower()]
    print(f"Employee names with 'e': {names_with_e}")

read_employees()