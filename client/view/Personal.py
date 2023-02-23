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

        self.print("\nName: " + str(self.__name))
        self.print("Username: " + str(self.__username))
        self.print("Email: " + str(self.__email))
        self.print("Employee ID: " + str(self.__employee_id))
        self.print("Last Login: " + str(self.__last_login), end="")

        self.add_option("Edit Name", self.__edit_name)
        self.add_option("Edit Username", self.__edit_username)
        self.add_option("Edit Email Address", self.__edit_email)

    def __edit_name(self):
        pass

    def __edit_username(self):
        pass

    def __edit_email(self):
        pass
