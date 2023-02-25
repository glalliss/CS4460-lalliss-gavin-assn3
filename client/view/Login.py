import tkinter as tk
from client.view.Menu import Menu
from client.view.MainMenu import MainMenu
from client.service.api import API


class Login(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Login", root, *args, **kwargs)

        self.__api = API()
        self.__username = ""

        self.get_root().title("Login")
        self.add_option("Login", self.get_input, 2, "Login", self.__login, "Username", "Password")
        self.add_option("\nExit", exit, 0)

    def __login(self, username, password):
        result = self.__api.login(username, password)
        self.__username = username
        if result == -1:
            self.set_display("\nERROR: Invalid Username or Password\nPlease try again")
        elif result == "New User":
            # change password from temporary
            self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")
        else:
            self.__api.update_login_timestamp(username)
            self.__switch_to_main(username)

    def __change_pw(self, new_pw, conf_pw):
        if new_pw == conf_pw:
            password = str(conf_pw)
            symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
            if any(letter.isupper() for letter in password) and any(letter.islower() for letter in password) and any(letter.isdigit() for letter in password) and any(letter in symbols for letter in password):
                self.__api.update_login_timestamp(self.__username)
                self.__api.update_password(self.__username, password)
                self.__switch_to_main(self.__username)
            else:
                self.set_display("\nERROR: New Password must contain an uppercase and lowercase letter, a number, and a symbol from the number keys")
                self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")
        else:
            self.set_display("\nERROR: Password must match")
            self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")

    def __switch_to_main(self, username):
        mm = MainMenu(self, self.get_root(), username)
        self.switch_menu(mm, self.__return_to_login)

    def __return_to_login(self):
        self.get_root().title("Login")
