# Testing storing data a certain way for app:
import json
import re
from pathlib import Path
import os

path = "./ec_expenses"
path1 = "./ec_sales"

files_exp = [f for f in os.listdir(path)]

files_sale = [f for f in os.listdir(path1)]
# print(files_exp)
# print(files_sale)

# x = files_exp[0]

# print(x[8:10])
start_date = "2022-08-13"
end_date = "2022-08-16"

y_start = start_date[:4]
m_start = start_date[5:7]
d_start = start_date[8:]
y_end = end_date[:4]
m_end = end_date[5:7]
d_end = end_date[8:]
files_in_range = []
if y_start == y_end:
    if m_start == m_end:
        date_range = range(int(d_start), int(d_end) + 1)
for file in files_exp:
    if file[8:10] >= d_start and file[8:10] <= d_end:
        files_in_range.append(file)
print(files_in_range)

for i in files_in_range:
    with open(f"ec_expenses/{i}", "r") as file:
        fileData = json.load(file)
        for x in fileData.keys():
            print(x)

"""
y_start = start_date[:4]
m_start = start_date[5:7]
d_start = start_date[8:]
y_end = end_date[:4]
m_end = end_date[5:7]
d_end = end_date[8:]
date_search = range(int(d_start), int(d_end) + 1)
re.findall("2022-08-")
dir = r"C:/Users/16092/OneDrive/Desktop/practice_kivy/ec_expenses"
file = Path(dir).glob("*")
matches = []
for x in file:
    if x == f"2022-08-{date_search}.expense_data.json":
        matches.append(x)
print(matches)


# ToDo: need to match files in given directory to date range specified by user;
"""
