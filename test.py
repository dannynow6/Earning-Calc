# Testing storing data a certain way for app:
import json
import re
from pathlib import Path


start_date = "2022-08-10"
end_date = "2022-08-14"

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
