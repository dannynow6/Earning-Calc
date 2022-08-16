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
# Expense info reporting tests
for file in files_exp:
    if file[8:10] >= d_start and file[8:10] <= d_end:
        files_in_range.append(file)
print(files_in_range)
expense_cost = []
expense_name = []
for i in files_in_range:
    with open(f"ec_expenses/{i}", "r") as file:
        fileData = json.load(file)
        for k in fileData.keys():
            exp_cost = float(fileData[k]["cost"])
            expense_name.append(k)
            expense_cost.append(exp_cost)
print(expense_cost)
print(type(expense_cost[0]))
print(sum(expense_cost))
print(expense_name)
print(len(expense_name), len(expense_cost))

print(
    f"List of expenses:\n{expense_name[0]}, cost: ${expense_cost[0]}\n{expense_name[1]}, cost: ${expense_cost[1]}\n...\nTotal Cost Expenses: {sum(expense_cost)}"
)

# Sale Info Reporting tests:
sales_in_range = []
sales_name = []
sales_amt_charged = []
sales_taxable = []

for file in files_sale:
    if file[8:10] >= d_start and file[8:10] <= d_end:
        sales_in_range.append(file)
print(sales_in_range)
for i in sales_in_range:
    with open(f"ec_sales/{i}", "r") as file:
        saleData = json.load(file)
        for k in saleData.keys():
            sales_name.append(k)
            amt_charged = float(saleData[k]["sale"])
            sales_amt_charged.append(amt_charged)
            est_tax = float(saleData[k]["est_sales_tax"])
            sales_taxable.append(est_tax)
print(sales_name)
print(sales_amt_charged)
print(sales_taxable)
