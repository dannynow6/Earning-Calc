# File name: main.py

from datetime import date
from kivymd.app import MDApp
from kivy.factory import Factory

from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
import json
import os


class EarningCalcApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_file("earningcalc.kv")

    current_date = date.today()
    now = current_date.strftime("%Y-%m-%d")
    user_email = ObjectProperty()
    sales_tax = NumericProperty()
    shop_percent = NumericProperty()
    expense_name = ObjectProperty()
    expense_cost = NumericProperty()
    expense_quantity = NumericProperty()
    current_expenses = {}
    customer_name = ObjectProperty()
    sale_amount = NumericProperty()
    deposit_amount = NumericProperty()

    def clear_settings(self):
        self.root.ids.name_input.text = ""
        self.root.ids.email_input.text = ""
        self.root.ids.sales_tax_input.text = ""
        self.root.ids.shop_percent_input.text = ""

    def clear_dates(self):
        self.root.ids._start_date.text = ""
        self.root.ids._end_date.text = ""

    user_info = JsonStore("ec_settings/user_settings.json")
    expenses_data = JsonStore(f"ec_expenses/{now}.expense_data.json")
    sale_info = JsonStore(f"ec_sales/{now}.sale_info.json")
    earning_reports = JsonStore(f"ec_reports/{now}.json")

    def generate_report(self):
        start_date = self.root.ids._start_date.text
        end_date = self.root.ids._end_date.text
        # From user input slice string to access just days specified
        d_start = start_date[8:]
        d_end = end_date[8:]
        # Create path variables for directories to be accessed
        path = "./ec_expenses"
        path1 = "./ec_sales"
        # Create lists of file names that fall within date range
        files_exp = [f for f in os.listdir(path)]
        files_sale = [f for f in os.listdir(path1)]

        # Add relevant expense files to list
        exp_in_range = [
            file for file in files_exp if file[8:10] >= d_start and file[8:10] <= d_end
        ]
        # Add relevant sales files to list
        sales_in_range = [
            file for file in files_sale if file[8:10] >= d_start and file[8:10] <= d_end
        ]
        # Create empty lists for storing data temporarily
        exp_cost = []
        exp_name = []
        sale_name = []
        sale_est_tax = []
        sale_amt_charged = []

        # Access data from expense files
        for i in exp_in_range:
            with open(f"ec_expenses/{i}", "r") as file:
                fileData = json.load(file)
                for k in fileData.keys():
                    exp = float(fileData[k]["cost"])
                    exp_name.append(k)
                    exp_cost.append(exp)
        # Access data from sales files
        for i in sales_in_range:
            with open(f"ec_sales/{i}", "r") as file:
                saleData = json.load(file)
                for k in saleData.keys():
                    sale_name.append(k)
                    amt_charged = float(saleData[k]["sale"])
                    sale_amt_charged.append(amt_charged)
                    est_tax = float(saleData[k]["est_sales_tax"])
                    sale_est_tax.append(est_tax)
        total_sales = float(sum(sale_amt_charged))
        total_est_tax = float(sum(sale_est_tax))
        total_exp = float(sum(exp_cost))
        # Create a formatted report - save temporarily in ec_reports directory
        self.earning_reports.put(
            "Earning Report",
            total_sales=f"${total_sales:.2f}",
            total_estimated_tax=f"${total_est_tax:.2f}",
            total_expenses=f"${total_exp:.2f}",
        )

    def save_user_info(self):
        self.user_info.put(
            "user_settings",
            name=self.root.ids.name_input.text,
            user_email=self.root.ids.email_input.text,
            sales_tax=self.root.ids.sales_tax_input.text,
            shop_percent=self.root.ids.shop_percent_input.text,
        )

    def exp_save(self):
        new_exp = self.root.ids.exp_name.text
        cost = float(self.root.ids.exp_cost.text)
        quantity_per = float(self.root.ids.exp_quantity.text)
        unit_cost = cost / quantity_per
        self.expenses_data.put(
            f"{new_exp}",
            cost=f"{cost:.2f}",
            quantity=f"{quantity_per}",
            cost_per=f"{unit_cost:.2f}",
        )
        self.root.ids.exp_name.text = ""
        self.root.ids.exp_quantity.text = ""
        self.root.ids.exp_cost.text = ""

    def sale_info_save(self):
        customer_name = self.root.ids.sale_name.text
        sale_amount = float(self.root.ids.amt_charged.text)
        deposit_amount = float(self.root.ids.amt_deposit.text)
        total_sale = sale_amount + deposit_amount
        with open("ec_settings/user_settings.json", "r") as file:
            userData = json.load(file)
        sales_tax = float(userData["user_settings"]["sales_tax"])
        shop_cut = float(userData["user_settings"]["shop_percent"])
        shop_owed = sale_amount * shop_cut
        est_tax = (sale_amount - shop_owed) * sales_tax
        est_earnings = total_sale - (shop_owed + est_tax)
        self.sale_info.put(
            f"{customer_name}",
            sale=f"{sale_amount:.2f}",
            deposit=f"{deposit_amount:.2f}",
            total=f"{total_sale:.2f}",
            shop_owed=f"{shop_owed:.2f}",
            est_sales_tax=f"{est_tax:.2f}",
            est_earnings=f"{est_earnings:.2f}",
        )
        self.root.ids.sale_name.text = ""
        self.root.ids.amt_charged.text = ""
        self.root.ids.amt_deposit.text = ""

    """  
    def gen_report(self):
        Need to generate a report by matching text input dates from user input to dates of saved files to grab all files within range. Use regular expression module to match dates at beginning of file name.
    """


if __name__ == "__main__":
    LabelBase.register(
        name="Roboto",
        fn_bold="Roboto/Roboto-Regular.ttf",
        fn_regular="Roboto/Roboto-Thin.ttf",
        fn_italic="Roboto/Roboto-LightItalic.ttf",
    )
    EarningCalcApp().run()
