# Testing storing data a certain way for app:
import json
import re

start_date = "2022-08-10"
end_date = "2022-08-14"

with open("ec_app_data/user_settings.json", "r") as file:
    jsonData = json.load(file)
print(jsonData["user_settings"]["user_email"])
print(jsonData["user_settings"]["sales_tax"])

try:
    with open("ec_app_data/user_settings.json", "r") as file:
        jsonData = json.load(file)
except FileNotFoundError:
    print("Sorry, no file")
