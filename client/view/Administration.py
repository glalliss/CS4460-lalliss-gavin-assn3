import tkinter as tk

from client.view.Calculations import Calculations
from client.view.EditUser import EditUser
from client.view.Menu import Menu
from client.service.api import API


class Administration(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, employee_id: str, *args, **kwargs) -> None:
        super().__init__(master, "Manage Users", root, *args, **kwargs)
        self.get_root().title("Menu")

        self.__api = API()
        self.__user_dict = self.__api.get_managers(employee_id)
        self.__employee_id = employee_id
        self.__filters = {
            "1": True,
            "2": True,
        }
        self.__job_title = {
            "1": "Administrator",
            "2": "Human Resources",
        }
        self.set_options_header("Add user or select a user to edit:")
        self.add_option("\nAdd Human Resources Employee", self.get_input, 3, "Add Info", self.__add_user, "Name", "Username", "Email")
        self.add_option("View Calculations", self.__get_calculations)
        self.add_option("\nFilter:\n[X] | Administrator", self.__filter, "1")
        self.add_option("[X] | Human Resources", self.__filter, "2")
        self.__populate_users()

    # add user with check every access control
    def __add_user(self, name, username, email):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access is not None:
            if str(name).replace(" ", "") != "" and str(username).replace(" ", "") != "" and str(email).replace(" ", "") != "":
                self.__api.add_user(name, username, email, 2, self.__employee_id)
                self.set_display(f"\nSuccessfully added {name} to the system\n")
                self.__rerender()
            else:
                self.set_display("\nERROR: One or more of the categories was left empty\n")
        else:
            self.set_display("\nYour access has been revoked for this function\n")
            self.clear_options()

    # get calculation option to switch to calculation history page with check every access control
    def __get_calculations(self):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access is not None:
            calc = Calculations(self, self.get_root(), self.__employee_id)
            self.switch_menu(calc)
        else:
            self.set_display("\nYour access has been revoked for this function\n")
            self.clear_options()

    def __rerender(self):
        self.clear_options()
        self.add_option("\nAdd Human Resources Employee", self.get_input, 3, "Add Info", self.__add_user, "Name", "Username", "Email")
        self.add_option("View Calculations", self.__get_calculations)
        if self.__filters["1"]: self.add_option("\nFilter:\n[X] | Administrator", self.__filter, "1")
        else: self.add_option("\nFilter:\n[ ] | Administrator", self.__filter, "1")
        if self.__filters["2"]: self.add_option("[X] | Human Resources", self.__filter, "2")
        else: self.add_option("[ ] | Human Resources", self.__filter, "2")
        self.__user_dict = self.__api.get_managers(self.__employee_id)
        self.__populate_users()

    # filter with check every access control
    def __filter(self, job_id):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access is not None:
            if self.__filters[job_id]:
                self.__filters[job_id] = False
                self.edit_option(int(job_id), name=f"[ ] | {self.__job_title[job_id]}")
            else:
                self.__filters[job_id] = True
                self.edit_option(int(job_id), name=f"[X] | {self.__job_title[job_id]}")
            self.__rerender()
        else:
            self.set_display("\nYour access has been revoked for this function\n")
            self.clear_options()

    # populate users but only human resources or admin
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
                self.add_option("\n" + name.ljust(30, ' ') + " - " + username.ljust(18, ' ') + " - " + self.__job_title[job_id], self.__edit_user, user_info_dict)
                first_time = 0
            else:
                self.add_option(name.ljust(30, ' ') + " - " + username.ljust(18, ' ') + " - " + self.__job_title[job_id], self.__edit_user, user_info_dict)

    # edit user with check every access control
    def __edit_user(self, user_info_dict):
        access = self.__api.get_personal_access_info(self.__employee_id).get("job_ID")
        if access is not None:
            if user_info_dict.get('job_ID') == "1":
                self.set_display("\nERROR: Nobody is allowed to edit Administrator accounts\n")
            else:
                eu = EditUser(self, self.get_root(), user_info_dict.get("employee_ID"), self.__employee_id)
                self.switch_menu(eu)
        else:
            self.set_display("\nYour access has been revoked for this function\n")
            self.clear_options()
