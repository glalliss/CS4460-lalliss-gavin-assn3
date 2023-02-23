import tkinter as tk
from client.view.Menu import Menu
from client.view.MainMenu import MainMenu
from client.service.api import API


class Login(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Login", root, *args, **kwargs)

        self.__api = API()

        self.get_root().title("Login")
        self.add_option("Login", self.get_input, 2, "Login", self.__login, "Username", "Password")
        self.add_option("Exit", exit, 0)

    def __login(self, username, password):
        result = self.__api.login(username, password)

        if result:
            self.__switch_to_main(username)
        else:
            self.set_display("Invalid Username or Password\nPlease try again")

    def __switch_to_main(self, username):
        mm = MainMenu(self, self.get_root(), username)
        self.switch_menu(mm, self.__return_to_login)

    def __return_to_login(self):
        self.get_root().title("Login")