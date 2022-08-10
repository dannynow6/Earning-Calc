# File name: main.py

from datetime import date
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.theming import ThemeManager

from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore
import json
from kivymd.uix.menu import MDDropdownMenu
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

    def clear_settings(self):
        self.root.ids.email_input.text = ""
        self.root.ids.sales_tax_input.text = ""
        self.root.ids.shop_percent_input.text = ""

    user_info = JsonStore("user_settings.json")
    expenses_data = JsonStore("expense_data.json")

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
            cost=self.root.ids.exp_cost.text,
            quantity=self.root.ids.exp_quantity.text,
            cost_per=("%.2f" % unit_cost),
        )
        self.root.ids.exp_name.text = ""
        self.root.ids.exp_quantity.text = ""
        self.root.ids.exp_cost.text = ""

    """
    def exp_list(self):
        expenses_menu = DropDown()
        with open("expense_data.json", "r") as file:
            expData = json.load(file)
        for i in expData.keys():
            btn = Button(text=i, size_hint_y=None, height=40)
            # btn.bind(on_release=lambda btn: expenses_menu.select(btn.text))
            expenses_menu.add_widget(btn)
        expenses_menu.open

    """


if __name__ == "__main__":
    LabelBase.register(
        name="Roboto",
        fn_bold="Roboto/Roboto-Regular.ttf",
        fn_regular="Roboto/Roboto-Thin.ttf",
        fn_italic="Roboto/Roboto-LightItalic.ttf",
    )
    EarningCalcApp().run()
