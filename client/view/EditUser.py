import tkinter as tk
from client.view.Menu import Menu
from client.service.api import API


class EditUser(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, user_dict: dict) -> None:
        super().__init__(master, "Edit User", root)
        self.get_root().title("Menu")

        self.__api = API()

        self.__job_titles = {
            "1": "Administrator",
            "2": "Human Resources",
            "3": "Junior Accountant",
            "4": "Senior Accountant",
            "5": "Junior Engineer",
            "6": "Senior Engineer",
            "7": "Mathematician",
        }

        self.__name = user_dict.get("name")
        self.__username = user_dict.get("username")
        self.__email = user_dict.get("email")
        self.__job_title = self.__job_titles.get(user_dict.get("job_ID"))
        self.__employee_id = user_dict.get("employee_ID")
        self.__last_login = user_dict.get("last_login")

        self.__print_info()

        self.add_option("Edit Name", self.get_input, 1, "Edit Name", self.__edit_name, "New Name")
        self.add_option("Edit Username", self.get_input, 1, "Edit Username", self.__edit_username, "New Username")
        self.add_option("Edit Email", self.get_input, 1, "Edit Email", self.__edit_email, "New Email")
        self.add_option("Edit Job Title", self.get_input, 1, "Edit Job Title", self.__edit_job_title, "3 = Junior Accountant\n4 = Senior Accountant\n5 = Junior Engineer\n6 = Senior Engineer\n7 = Mathematician")
        self.add_option("\nRemove User", self.__remove_user)

    def __print_info(self):
        self.print("\nName: " + str(self.__name))
        self.print("Username: " + str(self.__username))
        self.print("Email: " + str(self.__email))
        self.print("Job Title: " + str(self.__job_title))
        self.print("Employee ID: " + str(self.__employee_id))
        self.print("Last Login: " + str(self.__last_login), end="")

    def __edit_name(self, name):
        self.__api.update_name(self.__employee_id, name)
        self.__name = name
        self.clear_display()
        self.__print_info()

    def __edit_username(self, username):
        self.__api.update_username(self.__employee_id, username)
        self.__username = username
        self.clear_display()
        self.__print_info()

    def __edit_email(self, email):
        self.__api.update_email(self.__employee_id, email)
        self.__email = email
        self.clear_display()
        self.__print_info()

    def __edit_job_title(self, job_title):
        if str(job_title).isdigit():
            if int(job_title) in range(3, 8):
                self.__api.update_job_title(self.__employee_id, job_title)
                self.__job_title = self.__job_titles.get(job_title)
                self.clear_display()
                self.__print_info()
            else:
                self.set_display("\nERROR: Must enter digit between 3-7\n")
                self.__print_info()
        else:
            self.set_display("\nERROR: Must enter digit\n")
            self.__print_info()

    def __remove_user(self):
        self.__api.remove_user(self.__employee_id)
        self.clear_options()
        self.set_display("\nREMOVED USER")
