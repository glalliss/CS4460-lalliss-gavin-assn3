import tkinter as tk
from client.view.Menu import Menu
from client.service.api import API


class HumanResources(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Manage Users", root, *args, **kwargs)

        self.__api = API()
        self.__populate_users()
        # self.add_option("Add User")

    def __populate_users(self):
        self.clear_options()
        self.set_options_header("Select a user to edit:")

        result = self.__api.get_users()
        for user in result:
            user_info_dict = result.get(user)
            name = user_info_dict.get('name')
            username = user_info_dict.get('username')
            job_id = user_info_dict.get("job_ID")
            if job_id == "1":
                job_title = "Administrator"
            elif job_id == "2":
                job_title = "Human Resources"
            elif job_id == "3":
                job_title = "Junior Accountant"
            elif job_id == "4":
                job_title = "Senior Accountant"
            elif job_id == "5":
                job_title = "Junior Engineer"
            elif job_id == "6":
                job_title = "Senior Engineer"
            elif job_id == "7":
                job_title = "Mathematician"
            else:
                job_title = "Ex-employee"
            self.add_option(name.ljust(25, ' ') + " - " + username.ljust(15, ' ') + " - " + job_title, self.__edit_user, user_info_dict)

    def __edit_user(self, username):
        self.__selected_old_user = username
        self.get_input(1, f"Editing user: {username}", self.__process_edit, f"Enter a new username for account: {username}")

    def __process_edit(self, new_username):
        self.set_display("NOTE: Nothing was actually saved")




