import server.controller.controller as controller  # Fake network connection to server


class API:
    instance = None

    # Singleton management. This is called before __init__
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

#############################################################################################
# All Function calls will make a call on the controller and return to the view that called it
#############################################################################################

    # Login a user
    # Note: this is not implemented the way you need to do it
    def login(self, user, password):
        return controller.login(user, password)

    # Get list of users
    def get_users(self, performer):
        return controller.get_users(performer)

    def get_managers(self, performer):
        return controller.get_managers(performer)

    def add(self, num1, num2):
        return controller.add(num1, num2)

    def sub(self, num1, num2):
        return controller.sub(num1, num2)

    def mul(self, num1, num2):
        return controller.mul(num1, num2)

    def div(self, num1, num2):
        return controller.div(num1, num2)

    def get_personal_access_info(self, employee_id):
        return controller.get_personal_access_info(employee_id)

    def get_user_info(self, employee_id, performer):
        return controller.get_user_info(employee_id, performer)

    def add_user(self, name, username, email, job_id, performer):
        return controller.add_user(name, username, email, job_id, performer)

    def get_username(self, employee_id):
        return controller.get_username(employee_id)

    def update_name(self, employee_id, name, performer):
        controller.update_name(employee_id, name, performer)

    def update_username(self, employee_id, username, performer):
        controller.update_username(employee_id, username, performer)

    def update_email(self, employee_id, email, performer):
        controller.update_email(employee_id, email, performer)

    def update_job_title(self, employee_id, job_title, performer):
        controller.update_job_title(employee_id, job_title, performer)

    def remove_user(self, employee_id, performer):
        controller.remove_user(employee_id, performer)

    # Only used once for first login
    def update_password(self, username, password):
        controller.update_password(username, password)

    def update_login_timestamp(self, employee_id):
        controller.update_login_timestamp(employee_id)

    def update_calculations(self, employee_id, result, calc_type):
        controller.update_calculations(employee_id, result, calc_type)

    def log_calculation_page(self, employee_id):
        controller.log_calculation_page(employee_id)

    def populate_calculations(self, filter_dict, performer):
        return controller.populate_calculations(filter_dict, performer)
