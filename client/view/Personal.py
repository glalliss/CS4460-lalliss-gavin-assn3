import tkinter as tk
from client.view.Menu import Menu
from client.service.api import API


class Personal(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, employee_id: str) -> None:
        super().__init__(master, f"Personal Info", root)
        self.__api = API()
        user_dict = self.__api.get_user_info(employee_id, employee_id)

        self.get_root().title(f"Menu")

        self.__name = user_dict.get("name")
        self.__username = user_dict.get("username")
        self.__email = user_dict.get("email")
        self.__employee_id = user_dict.get("employee_ID")
        self.__last_login = user_dict.get("last_login")

        self.__print_info()

        self.add_option("Edit Name", self.get_input, 1, "Edit Name", self.__edit_name, "New Name")
        self.add_option("Edit Username", self.get_input, 1, "Edit Username", self.__edit_username, "New Username")
        self.add_option("Edit Email", self.get_input, 1, "Edit Email", self.__edit_email, "New Email")

    def __print_info(self):
        self.print("\nName: " + str(self.__name))
        self.print("Username: " + str(self.__username))
        self.print("Email: " + str(self.__email))
        self.print("Employee ID: " + str(self.__employee_id))
        self.print("Last Login: " + str(self.__last_login), end="")

    def __edit_name(self, name):
        self.__api.update_name(self.__employee_id, name, self.__employee_id)
        self.__name = name
        self.clear_display()
        self.__print_info()

    def __edit_username(self, username):
        self.__api.update_username(self.__employee_id, username, self.__employee_id)
        self.__username = username
        self.clear_display()
        self.__print_info()

    def __edit_email(self, email):
        self.__api.update_email(self.__employee_id, email, self.__employee_id)
        self.__email = email
        self.clear_display()
        self.__print_info()
