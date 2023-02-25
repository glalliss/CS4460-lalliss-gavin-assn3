import tkinter as tk

from client.view.EditUser import EditUser
from client.view.Menu import Menu
from client.service.api import API


class HumanResources(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Manage Users", root, *args, **kwargs)

        self.get_root().title("Menu")

        self.__api = API()
        self.__user_dict = self.__api.get_users()
        self.__filters = {
            "1": True,
            "2": True,
            "3": True,
            "4": True,
            "5": True,
            "6": True,
            "7": True,
        }
        self.__job_title = {
            "1": "Administrator",
            "2": "Human Resources",
            "3": "Junior Accountant",
            "4": "Senior Accountant",
            "5": "Junior Engineer",
            "6": "Senior Engineer",
            "7": "Mathematician",
        }
        self.set_options_header("Add user or select a user to edit:")
        self.add_option("\nAdd User", self.get_input, 4, "Add Info", self.__add_user, "Name", "Username", "Email", "Job Title:\n3 = Junior Accountant\n4 = Senior Accountant\n5 = Junior Engineer\n6 = Senior Engineer\n7 = Mathematician")
        self.add_option("\nFilter:\n[X] | Administrator", self.__filter, "1")
        self.add_option("[X] | Human Resources", self.__filter, "2")
        self.add_option("[X] | Junior Accountant", self.__filter, "3")
        self.add_option("[X] | Senior Accountant", self.__filter, "4")
        self.add_option("[X] | Junior Engineer", self.__filter, "5")
        self.add_option("[X] | Senior Engineer", self.__filter, "6")
        self.add_option("[X] | Mathematician", self.__filter, "7")
        self.__populate_users()

    def __add_user(self, name, username, email, job_id):
        if str(name).replace(" ", "") != "" and str(username).replace(" ", "") != "" and str(email).replace(" ", "") != "":
            if str(job_id).isdigit():
                if int(job_id) in range(3, 8):
                    self.__api.add_user(name, username, email, job_id)
                    self.set_display(f"\nSuccessfully added {name} to the system\n")
                else:
                    self.set_display("\nERROR: Must enter digit between 3-7 for Job Title\n")
            else:
                self.set_display("\nERROR: Must enter digit for Job Title\n")
        else:
            self.set_display("\nERROR: One or more of the categories was left empty\n")

    def __rerender(self):
        self.clear_options()
        self.add_option("\nAdd User", self.get_input, 4, "Add Info", self.__add_user, "Name", "Username", "Email", "Job Title:\n3 = Junior Accountant\n4 = Senior Accountant\n5 = Junior Engineer\n6 = Senior Engineer\n7 = Mathematician")
        if self.__filters["1"]: self.add_option("\nFilter:\n[X] | Administrator", self.__filter, "1")
        else: self.add_option("\nFilter:\n[ ] | Administrator", self.__filter, "1")
        if self.__filters["2"]: self.add_option("[X] | Human Resources", self.__filter, "2")
        else: self.add_option("[ ] | Human Resources", self.__filter, "2")
        if self.__filters["3"]: self.add_option("[X] | Junior Accountant", self.__filter, "3")
        else: self.add_option("[ ] | Junior Accountant", self.__filter, "3")
        if self.__filters["4"]: self.add_option("[X] | Senior Accountant", self.__filter, "4")
        else: self.add_option("[ ] | Senior Accountant", self.__filter, "4")
        if self.__filters["5"]: self.add_option("[X] | Junior Engineer", self.__filter, "5")
        else: self.add_option("[ ] | Junior Engineer", self.__filter, "5")
        if self.__filters["6"]: self.add_option("[X] | Senior Engineer", self.__filter, "6")
        else: self.add_option("[ ] | Senior Engineer", self.__filter, "6")
        if self.__filters["7"]: self.add_option("[X] | Mathematician", self.__filter, "7")
        else: self.add_option("[ ] | Mathematician", self.__filter, "7")
        self.__populate_users()

    def __filter(self, job_id):
        if self.__filters[job_id]:
            self.__filters[job_id] = False
            self.edit_option(int(job_id), name=f"[ ] | {self.__job_title[job_id]}")
        else:
            self.__filters[job_id] = True
            self.edit_option(int(job_id), name=f"[X] | {self.__job_title[job_id]}")
        self.__rerender()

    def __populate_users(self):
        first_time = 1
        for user in self.__user_dict:
            user_info_dict = self.__user_dict.get(user)
            name = user_info_dict.get('name')
            username = user_info_dict.get('username')
            job_id = user_info_dict.get("job_ID")
            if not self.__filters[job_id]:
                continue
            if first_time == 1:
                self.add_option("\n" + name.ljust(30, ' ') + " - " + username.ljust(20, ' ') + " - " + self.__job_title[job_id], self.__edit_user, user_info_dict)
                first_time = 0
            else:
                self.add_option(name.ljust(30, ' ') + " - " + username.ljust(20, ' ') + " - " + self.__job_title[job_id], self.__edit_user, user_info_dict)

    def __edit_user(self, user_info_dict):
        if user_info_dict.get('job_ID') == "1":
            self.set_display("\nERROR: Nobody is allowed to edit Administrator accounts\n")
        elif user_info_dict.get('job_ID') == "2":
            self.set_display("\nERROR: Only Administrators are allowed to edit HR accounts\n")
        else:
            eu = EditUser(self, self.get_root(), user_info_dict)
            self.switch_menu(eu)

    def __return_to_human_resources(self):
        self.get_root().title("Human Resources")
