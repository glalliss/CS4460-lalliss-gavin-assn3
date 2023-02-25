import tkinter as tk

from client.view.Menu import Menu
from client.service.api import API


class Calculations(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Calculations", root, *args, **kwargs)

        self.get_root().title("Menu")

        self.__api = API()

        self.__filters = {
            "1": True,
            "2": True,
            "3": True,
            "4": True,
        }
        self.__calculation_title = {
            "1": "Addition",
            "2": "Subtraction",
            "3": "Multiplication",
            "4": "Division",
        }
        self.add_option("Filter:\n[X] | Addition", self.__filter, "1")
        self.add_option("[X] | Subtraction", self.__filter, "2")
        self.add_option("[X] | Multiplication", self.__filter, "3")
        self.add_option("[X] | Division", self.__filter, "4")
        self.__populate_calculations()

    def __rerender(self):
        self.clear_options()

        if self.__filters["1"]: self.add_option("\nFilter:\n[X] | Addition", self.__filter, "1")
        else: self.add_option("Filter:\n[ ] | Addition", self.__filter, "1")
        if self.__filters["2"]: self.add_option("[X] | Subtraction", self.__filter, "2")
        else: self.add_option("[ ] | Subtraction", self.__filter, "2")
        if self.__filters["3"]: self.add_option("[X] | Multiplication", self.__filter, "3")
        else: self.add_option("[ ] | Multiplication", self.__filter, "3")
        if self.__filters["4"]: self.add_option("[X] | Division", self.__filter, "4")
        else: self.add_option("[ ] | Division", self.__filter, "4")
        self.__populate_calculations()

    def __filter(self, calc_num):
        if self.__filters[calc_num]:
            self.__filters[calc_num] = False
            self.edit_option(int(calc_num)-1, name=f"[ ] | {self.__calculation_title[calc_num]}")
        else:
            self.__filters[calc_num] = True
            self.edit_option(int(calc_num)-1, name=f"[X] | {self.__calculation_title[calc_num]}")
        self.__rerender()

    def __populate_calculations(self):
        calc_dict = self.__api.populate_calculations(self.__filters)
        first = "Date/Time"
        second = "username"
        third = "calculation"
        self.set_display(f"\n{first.ljust(22, ' ')} | {second.ljust(20, ' ')} | {third}\n")
        for calculation in calc_dict:
            date_time = calc_dict.get(calculation)[0]
            employee_id = calc_dict.get(calculation)[1]
            calc = calc_dict.get(calculation)[2]
            self.print(f"{date_time} | {self.__api.get_username(employee_id).ljust(20, ' ')} | {calc}")
