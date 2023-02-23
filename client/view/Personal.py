import tkinter as tk
from client.view.Menu import Menu
from client.service.api import API


class Personal(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, username: str) -> None:
        super().__init__(master, f"Personal Info for {username}", root)

        self.__api = API()

        self.get_root().title(f"Personal Info for {username}")

        user_dict = self.__api.get_user_info(username)
        self.__name = user_dict.get("name")
        self.__username = user_dict.get("username")
        self.__email = user_dict.get("email")
        self.__employee_id = user_dict.get("employee_ID")
        self.__last_login = user_dict.get("last_login")

        self.set_display("Name: " + str(self.__name))
        self.set_display("Username: " + str(self.__username))
        self.set_display("Email: " + str(self.__email))
        self.set_display("Employee ID: " + str(self.__employee_id))
        self.set_display("Last Login: " + str(self.__last_login))
