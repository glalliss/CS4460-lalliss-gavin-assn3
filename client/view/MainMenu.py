import tkinter as tk

from client.view.Administration import Administration
from client.view.Menu import Menu
from client.view.HumanResources import HumanResources
from client.view.Personal import Personal
from client.service.api import API


class MainMenu(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, employee_id: str) -> None:
        self.__api = API()
        user_dict = self.__api.get_personal_access_info(employee_id)
        self.__user_dict = user_dict
        self.__employee_id = self.__user_dict.get('employee_ID')
        super().__init__(master, f"Welcome {self.__user_dict.get('name')}", root)
        self.get_root().title("Menu")

        # Administration page option
        if self.__user_dict.get('job_ID') == "1":
            self.add_option("Administration", self.__admin)
        # Human Resources page option
        if self.__user_dict.get('job_ID') == "1" or self.__user_dict.get('job_ID') == "2":
            self.add_option("Human Resources", self.__hr)
        # Addition option
        if self.__user_dict.get('job_ID') == "3" or self.__user_dict.get('job_ID') == "4" or self.__user_dict.get('job_ID') == "7":
            self.add_option("Add", self.get_input, 2, "Add", self.__add, "Num1", "Num2")
        # Subtraction option
        if self.__user_dict.get('job_ID') == "4" or self.__user_dict.get('job_ID') == "7":
            self.add_option("Subtract", self.get_input, 2, "Subtract", self.__sub, "Num1", "Num2")
        # Multiplication option
        if self.__user_dict.get('job_ID') == "5" or self.__user_dict.get('job_ID') == "6" or self.__user_dict.get('job_ID') == "7":
            self.add_option("Multiply", self.get_input, 2, "Multiply", self.__mul, "Num1", "Num2")
        # Division option
        if self.__user_dict.get('job_ID') == "6" or self.__user_dict.get('job_ID') == "7":
            self.add_option("Divide", self.get_input, 2, "Divide", self.__div, "Num1", "Num2")
        # Personal information page option
        self.add_option("Personal", self.__personal, employee_id)

    # transition to admin page with check every access control
    def __admin(self):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "1":
            admin = Administration(self, self.get_root(), self.__employee_id)
            self.switch_menu(admin)
        else:
            self.set_display("\nYour access has been revoked for this page")
            self.clear_options()

    # transition to hr page with check every access control
    def __hr(self):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "1" or access == "2":
            hr = HumanResources(self, self.get_root(), self.__employee_id)
            self.switch_menu(hr)
        else:
            self.set_display("\nYour access has been revoked for this page")
            self.clear_options()

    # add with check every access control and other logic to protect against errors
    def __add(self, num1, num2):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "3" or access == "4" or access == "7":
            test_num1 = str(num1).replace(".", "")
            test_num1 = str(test_num1).replace("-", "")
            test_num2 = str(num2).replace(".", "")
            test_num2 = str(test_num2).replace("-", "")
            if test_num1.isnumeric() and test_num2.isnumeric():
                result = self.__api.add(num1, num2)
                result = f"{num1} + {num2} = {result}"
                self.set_display(f"\n{result}")
                self.__api.update_calculations(self.__employee_id, result, 1)
            else:
                self.set_display("\nERROR: You must enter two numbers")
        else:
            self.set_display("\nYour access has been revoked for this function")
            self.clear_options()

    # subtract with check every access control and other logic to protect against errors
    def __sub(self, num1, num2):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "4" or access == "7":
            test_num1 = str(num1).replace(".", "")
            test_num1 = str(test_num1).replace("-", "")
            test_num2 = str(num2).replace(".", "")
            test_num2 = str(test_num2).replace("-", "")
            if test_num1.isnumeric() and test_num2.isnumeric():
                result = self.__api.sub(num1, num2)
                result = f"{num1} - {num2} = {result}"
                self.set_display(f"\n{result}")
                self.__api.update_calculations(self.__employee_id, result, 2)
            else:
                self.set_display("\nERROR: You must enter two numbers")
        else:
            self.set_display("\nYour access has been revoked for this function")
            self.clear_options()

    # multiply with check every access control and other logic to protect against errors
    def __mul(self, num1, num2):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "5" or access == "6" or access == "7":
            test_num1 = str(num1).replace(".", "")
            test_num1 = str(test_num1).replace("-", "")
            test_num2 = str(num2).replace(".", "")
            test_num2 = str(test_num2).replace("-", "")
            if test_num1.isnumeric() and test_num2.isnumeric():
                result = self.__api.mul(num1, num2)
                result = f"{num1} * {num2} = {result}"
                self.set_display(f"\n{result}")
                self.__api.update_calculations(self.__employee_id, result, 3)
            else:
                self.set_display("\nERROR: You must enter two numbers")
        else:
            self.set_display("\nYour access has been revoked for this function")
            self.clear_options()

    # divide with check every access control and other logic to protect against errors
    def __div(self, num1, num2):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access == "6" or access == "7":
            test_num1 = str(num1).replace(".", "")
            test_num1 = str(test_num1).replace("-", "")
            test_num2 = str(num2).replace(".", "")
            test_num2 = str(test_num2).replace("-", "")
            if test_num1.isnumeric() and test_num2.isnumeric():
                if int(test_num2) != 0:
                    result = self.__api.div(num1, num2)
                    result = f"{num1} / {num2} = {result}"
                    self.set_display(f"\n{result}")
                    self.__api.update_calculations(self.__employee_id, result, 4)
                else:
                    self.set_display("\nERROR: You cannot divide by zero")
            else:
                self.set_display("\nERROR: You must enter two numbers")
        else:
            self.set_display("\nYour access has been revoked for this function")
            self.clear_options()

    # transition to personal page with check every access control
    def __personal(self, employee_id):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access is not None:
            personal = Personal(self, self.get_root(), employee_id)
            self.switch_menu(personal)
        else:
            self.set_display("\nYour access has been revoked for this function")
            self.clear_options()
