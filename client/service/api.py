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
    def get_users(self):
        return controller.get_users()

    def add(self, num1, num2):
        return controller.add(num1, num2)

    def sub(self, num1, num2):
        return controller.sub(num1, num2)

    def mul(self, num1, num2):
        return controller.mul(num1, num2)

    def div(self, num1, num2):
        return controller.div(num1, num2)

    def get_user_info(self, username):
        return controller.get_user_info(username)

    def add_user(self, name, username, email, job_id):
        return controller.add_user(name, username, email, job_id)

    def update_name(self, username, name):
        controller.update_name(username, name)

    def update_username(self, old_username, new_username):
        controller.update_username(old_username, new_username)

    def update_email(self, username, email):
        controller.update_email(username, email)

    def update_job_title(self, username, job_title):
        controller.update_job_title(username, job_title)

    def remove_user(self, username):
        controller.remove_user(username)

    # Only used once for first login
    def update_password(self, username, password):
        controller.update_password(username, password)

    def update_login_timestamp(self, username):
        controller.update_login_timestamp(username)
