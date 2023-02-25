import tkinter as tk

from client.view.Menu import Menu
from client.service.api import API


class Calculations(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Calculations", root, *args, **kwargs)

        self.get_root().title("Menu")

        self.__api = API()
        self.__calc_dict = self.__api.get_calculations()

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
        self.add_option("\nFilter:\n[X] | Addition", self.__filter, "1")
        self.add_option("[X] | Subtraction", self.__filter, "2")
        self.add_option("[X] | Multiplication", self.__filter, "3")
        self.add_option("[X] | Division", self.__filter, "4")
        self.__populate_calculations()

    def __rerender(self):
        self.clear_options()

        if self.__filters["1"]: self.add_option("\nFilter:\n[X] | Addition", self.__filter, "1")
        else: self.add_option("\nFilter:\n[ ] | Addition", self.__filter, "1")
        if self.__filters["2"]: self.add_option("[X] | Subtraction", self.__filter, "2")
        else: self.add_option("[ ] | Subtraction", self.__filter, "2")
        if self.__filters["3"]: self.add_option("[X] | Multiplication", self.__filter, "3")
        else: self.add_option("[ ] | Multiplication", self.__filter, "3")
        if self.__filters["4"]: self.add_option("[X] | Division", self.__filter, "4")
        else: self.add_option("[ ] | Division", self.__filter, "4")
        first_time = 1
        for user in self.__calc_dict:
            user_info_dict = self.__calc_dict.get(user)
            name = user_info_dict.get('name')
            username = user_info_dict.get('username')
            job_id = user_info_dict.get("job_ID")
            if not self.__filters[job_id]:
                continue
            if first_time == 1:
                self.add_option("\n" + name.ljust(30, ' ') + " - " + username.ljust(20, ' ') + " - " + self.__calculation_title[job_id], self.__edit_user, user_info_dict)
                first_time = 0
            else:
                self.add_option(name.ljust(30, ' ') + " - " + username.ljust(20, ' ') + " - " + self.__calculation_title[job_id], self.__edit_user, user_info_dict)

    def __filter(self, job_id):
        if self.__filters[job_id]:
            self.__filters[job_id] = False
            self.edit_option(int(job_id), name=f"[ ] | {self.__calculation_title[job_id]}")
        else:
            self.__filters[job_id] = True
            self.edit_option(int(job_id), name=f"[X] | {self.__calculation_title[job_id]}")
        self.__rerender()

    def __populate_calculations(self):
        self.set_options_header("Calculations:")

        first_time = 1
        for calc in self.__calc_dict:
            calc_dict = self.__calc_dict.get(calc)
            time = calc_dict.get('timestamp')
            username = calc_dict.get('username')
            result = calc_dict.get("result")
            if first_time == 1:
                self.print("\n" + time + " - " + username.ljust(20, ' ') + " - " + self.__calc_dict[time])
                first_time = 0
            else:
                self.print(time + " - " + username.ljust(20, ' ') + " - " + self.__calc_dict[time])
