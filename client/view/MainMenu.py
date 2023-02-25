import tkinter as tk

from client.view.Menu import Menu
from client.view.HumanResources import HumanResources
from client.view.Personal import Personal
from client.service.api import API


class MainMenu(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, username: str) -> None:
        self.__api = API()
        user_dict = self.__api.get_user_info(username)
        super().__init__(master, f"Welcome {user_dict.get('name')}", root)

        self.get_root().title(f"Welcome {user_dict.get('name')}")

        # Administration
        if user_dict.get('job_ID') == "1":
            # self.add_option("Administration", self.__admin)
            pass
        # Human Resources
        if user_dict.get('job_ID') == "1" or user_dict.get('job_ID') == "2":
            self.add_option("Human Resources", self.__hr)
            self.add_option("Example IO", self.get_input, 1, "Example io", self.__io, "Enter the number of input prompts to test")
        # Add
        if user_dict.get('job_ID') == "3" or user_dict.get('job_ID') == "4" or user_dict.get('job_ID') == "7":
            self.add_option("Add", self.get_input, 2, "Add", self.__add, "Num1", "Num2")
        # Subtract
        if user_dict.get('job_ID') == "4" or user_dict.get('job_ID') == "7":
            self.add_option("Subtract", self.get_input, 2, "Subtract", self.__sub, "Num1", "Num2")
        # Multiply
        if user_dict.get('job_ID') == "5" or user_dict.get('job_ID') == "6" or user_dict.get('job_ID') == "7":
            self.add_option("Multiply", self.get_input, 2, "Multiply", self.__mul, "Num1", "Num2")
        # Divide
        if user_dict.get('job_ID') == "6" or user_dict.get('job_ID') == "7":
            self.add_option("Divide", self.get_input, 2, "Divide", self.__div, "Num1", "Num2")
        # Personal
        self.add_option("Personal", self.__personal, username)

    def __io(self, number_of_prompts: str):
        num = int(number_of_prompts)

        self.get_input(num, f"Testing with {num} inputs", self.__io1, *[f"Prompt #{i}" for i in range(num)])

    def __io1(self, *inputs):
        self.clear_display()
        self.print(f"You asked for {len(inputs)} inputs")
        
        for answer_index in range(len(inputs)):
            self.print(f"\tInput #{answer_index}:")
            self.print(f"\t\t{inputs[answer_index]}")

    # def __admin(self):
    #     admin = Admin(self, self.get_root())
    #     self.switch_menu(admin)

    def __hr(self):
        hr = HumanResources(self, self.get_root())
        self.switch_menu(hr)

    def __add(self, num1, num2):
        result = self.__api.add(num1, num2)
        self.set_display("\nThe result of the addition is " + str(result))

    def __sub(self, num1, num2):
        result = self.__api.sub(num1, num2)
        self.set_display("\nThe result of the subtraction is " + str(result))

    def __mul(self, num1, num2):
        result = self.__api.mul(num1, num2)
        self.set_display("\nThe result of the multiplication is " + str(result))

    def __div(self, num1, num2):
        result = self.__api.div(num1, num2)
        self.set_display("\nThe result of the division is " + str(result))

    def __personal(self, username):
        personal = Personal(self, self.get_root(), username)
        self.switch_menu(personal, self.__return_to_main_menu(username))

    def __return_to_main_menu(self, username):
        self.get_root().title(f"User: {username}")
