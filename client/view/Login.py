import tkinter as tk
from client.view.Menu import Menu
from client.view.MainMenu import MainMenu
from client.service.api import API


class Login(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Login", root, *args, **kwargs)
        self.get_root().title("Menu")

        self.__api = API()
        # create initial login title/menu and add options to login or exit
        self.add_option("Login", self.get_input, 2, "Login", self.__login, "Username", "Password")
        self.add_option("\nExit", exit, 0)

    # call login method from control and return based on information input by user
    def __login(self, username, password):
        result = self.__api.login(username, password)
        # invalid username or password so try again
        if result == -1:
            self.set_display("\nERROR: Invalid Username or Password\nPlease try again")
        # change password from temporary password to strong password
        elif result[1] == "73Mp()R@rY":
            self.__employee_id = result[2]
            self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")
        # login success for returning user
        else:
            self.__employee_id = result[2]
            self.__api.update_login_timestamp(self.__employee_id)
            self.__switch_to_main(self.__employee_id)

    # change password and check for strength and free of typos
    def __change_pw(self, new_pw, conf_pw):
        if new_pw == conf_pw:
            password = str(conf_pw)
            symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
            if any(letter.isupper() for letter in password) and any(letter.islower() for letter in password) and any(letter.isdigit() for letter in password) and any(letter in symbols for letter in password) and len(password) > 8:
                self.__api.update_login_timestamp(self.__employee_id)
                self.__api.update_password(self.__employee_id, password)
                self.__switch_to_main(self.__employee_id)
            else:
                self.set_display("\nERROR: New Password must be at least 9 characters long and contain an uppercase and lowercase letter, a number, and a symbol from the number keys")
                self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")
        else:
            self.set_display("\nERROR: Password must match")
            self.get_input(2, "Change Password", self.__change_pw, "New Password", "Confirm New Password")

    # switch to main menu and return to login page with information below
    def __switch_to_main(self, employee_id):
        mm = MainMenu(self, self.get_root(), employee_id)
        self.switch_menu(mm, self.__return_to_login)

    def __return_to_login(self):
        self.get_root().title("Menu")
