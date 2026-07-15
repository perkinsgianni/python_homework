# Task 2: Read a CSV File

import csv

def read_employees():
    employees_dict = {}
    employees_rows = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)

            # iterate through employees csv file
            for i, row in enumerate(reader):
                # create column headers in employees_dict
                if i == 0:
                    employees_dict["fields"] = row
                    # print(f"Task 2 | Employee dict fields: {employees_dict["fields"]}")
                else: 
                    # add rows to employees_rows list
                    employees_rows.append(row)
                    # print(f"Task 2 | Employee row(s): {employees_rows}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # add list of rows to employees_dict
    employees_dict["rows"] = employees_rows
    return employees_dict

employees = read_employees()
# print(f"Task 2 | Employees dict: {employees}")

#//////////////////////////////////////

# Task 3: Find the Column Index

def column_index(header):
    return employees["fields"].index(header)

employee_id_column = column_index("employee_id")
# employee_id_column = column_index("first_name")
# employee_id_column = column_index("last_name")
# employee_id_column = column_index("phone")
# print(f"Task 3 | Employee ID column: {employee_id_column}")

#//////////////////////////////////////

# Task 4: Find the Employee First Name

def first_name(row_number):
    # get index of first name column
    index = column_index("first_name")
    # print(f"Task 4 | Column index: {index}")

    # get employee at row_number
    employee = employees["rows"][row_number]
    # print(f"Task 4 | Employee: {employee}")

    # return name at index 
    return employee[index]
    # print(f"Task 4 | Employee first name: {employee[index]}")

# first_name(0)
# first_name(8)

#//////////////////////////////////////

# Task  5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):
        # iterate through rows, returns bool if row matches employee_id
        return int(row[employee_id_column]) == employee_id
        # print(f"Task 5 | Row match: {int(row[employee_id_column]) == employee_id}")

    # filter matches, convert to list
    matches = list(filter(employee_match, employees["rows"]))
    # print(f"Task 5 | Match: {matches}")

    return matches

# employee_find(1)
# employee_find(9)

#//////////////////////////////////////

# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))
    # print(f"Task 6 | Match: {matches}")

    return matches

# employee_find_2(1)
# employee_find_2(9)

#//////////////////////////////////////

# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    employees["rows"].sort(key=lambda row : row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()
# print(f"Task 7 | Sorted employees: {employees}")

#//////////////////////////////////////

# Task 8: Create a dict for an Employee

def employee_dict(row):
    single_employee_dict = {}
    # print(f"Task 8 | Employee ID column: {employee_id_column}")

    # iterate through column headers of employees dict
    for i, field in enumerate(employees["fields"]):
        # if employee_id, skip
        if i == employee_id_column:
            continue
        # add values to single_employee_dict
        single_employee_dict[field] = row[i]
        # print(f"Task 8 | Employee data: {single_employee_dict[field]}")

    # print(f"Task 8 | Employee dict: {single_employee_dict}")
    return single_employee_dict

print(employee_dict(employees["rows"][9]))
print(employee_dict(employees["rows"][1]))

#//////////////////////////////////////

# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    dict_of_dict = {}
    
    # iterate through rows in employees dict
    for row in employees["rows"]:
        # get employee_id
        employee_id = row[employee_id_column]
        # print(f"Task 9 | Employee ID: {employee_id}")

        # add values to dict_of_dict
        dict_of_dict[employee_id] = employee_dict(row)
        # print(f"Task 9 | Employee dict: {dict_of_dict[employee_id]}")

    # print(f"Task 9 | Employee dict of dict: {dict_of_dict}")
    return dict_of_dict

print(all_employees_dict())

#//////////////////////////////////////

# Task 10: Use the os Module

import os

def get_this_value():
    # print(f"Task 10 | THISVALUE: {os.getenv('THISVALUE')}")
    return os.getenv('THISVALUE')

# get_this_value()

#//////////////////////////////////////

# Task 11: Creating Your Own Module

import custom_module

def set_that_secret(new_secret):
    # call custom_module.set_secret() func, pass new_secret param
    custom_module.set_secret(new_secret)

# pass new secret
set_that_secret("This lesson is quite challenging.")
print(f"Task 11 | Secret: {custom_module.secret}")

#//////////////////////////////////////

# Task 12: Read minutes1.csv and minutes2.csv

# helper function to read each file
def read_minutes_file(file_path):
    minutes_dict = {}
    minutes_rows = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)

            # iterate through csv file
            for i, row in enumerate(reader):
                # create column headers
                if i == 0:
                    minutes_dict["fields"] = row
                    # print(f"Task 12 | Minutes dict fields: {minutes_dict["fields"]}")
                else: 
                    # convert rows to tuples, add to minutes_rows list
                    minutes_rows.append(tuple(row))
                    # # print(f"Task 12 | Minutes dict row(s) type: {type(minutes_rows)}")
                    # print(f"Task 12 | Minutes dict row(s): {minutes_rows}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # add list of rows to minutes_dict
    minutes_dict["rows"] = minutes_rows
    
    # print(f"Task 12 | Minutes dict: {minutes_dict}")
    return minutes_dict

def read_minutes():
    # pass file paths to helper function
    minutes1 = read_minutes_file('../csv/minutes1.csv')
    minutes2 = read_minutes_file('../csv/minutes2.csv')
    
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(f"Task 12 | Minutes1 dict: {minutes1}")
print(f"Task 12 | Minutes2 dict: {minutes2}")

#//////////////////////////////////////

# Task 13: Read minutes1.csv and minutes2.csv

def create_minutes_set():
    # convert minutes1, minutes2 rows to sets
    minutes1_set = set(minutes1["rows"])
    # print(f"Task 13 | Minutes1 set: {minutes1_set}")
    minutes2_set = set(minutes2["rows"])
    # print(f"Task 13 | Minutes2 set: {minutes2_set}")

    # join sets
    return minutes1_set.union(minutes2_set)
    # print(f"Task 13 | Minutes set: {minutes1_set.union(minutes2_set)}")

minutes_set = create_minutes_set()
# print(f"Task 13 | Minutes set: {minutes_set}")

#//////////////////////////////////////

# Task 14: Convert to datetime

from datetime import datetime

def create_minutes_list():
    # convert minutes set to list
    minutes_set_list = list(minutes_set)
    # convert to tuple: keep first element, convert date str to datetime obj
    datetime_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set_list))

    # print(f"Task 14 | Datetime list: {datetime_list}")
    return datetime_list

minutes_list = create_minutes_list()
print(f"Task 14 | Datetime list: {minutes_list}")

#//////////////////////////////////////

# Task 15: Write Out Sorted List

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    sorted_minutes_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    # print(f"Task 15 | Sorted date list: {sorted_minutes_list}")

    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file)

        # write header row from minutes1 dict
        writer.writerow(minutes1["fields"])

        # write subsequent rows from sorted_minutes_list
        for row in sorted_minutes_list:
            writer.writerow(row)

    # create list
    converted_list = []

    # append data rows from sorted_minutes_list
    for row in sorted_minutes_list:
        converted_list.append(row)

    # print(f"Task 15 | Converted list: {converted_list}")
    return converted_list

write_sorted_list()