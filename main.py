# File name: main.py

from datetime import date
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.theming import ThemeManager

from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
import json
from kivy.uix.gridlayout import GridLayout

"""  
with open("expense_data.json", "r") as file:
            expData = json.load(file)
            self.items = [f"{i}" for i in expData.keys()]

"""


class EarningCalcApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Blue"

        return Builder.load_file("earningcalc.kv")

    now = date.today()
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
        self.root.ids.email_input.text = ""
        self.root.ids.sales_tax_input.text = ""
        self.root.ids.shop_percent_input.text = ""

    user_info = JsonStore("user_settings.json")
    expenses_data = JsonStore("expense_data.json")
    sale_info = JsonStore("sale_info.json")

    def save_user_info(self):
        self.user_info.put(
            "user_settings",
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
        self.sale_info.put(
            f"{customer_name}",
            sale=f"{sale_amount:.2f}",
            deposit=f"{deposit_amount:.2f}",
            total=f"{total_sale:.2f}",
        )
        self.root.ids.sale_name.text = ""
        self.root.ids.amt_charged.text = ""
        self.root.ids.amt_deposit.text = ""


if __name__ == "__main__":
    LabelBase.register(
        name="Roboto",
        fn_bold="Roboto/Roboto-Regular.ttf",
        fn_regular="Roboto/Roboto-Thin.ttf",
        fn_italic="Roboto/Roboto-LightItalic.ttf",
    )
    EarningCalcApp().run()
