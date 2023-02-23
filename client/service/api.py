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
        info = controller.login(user, password)
        return info

    # Get list of users
    def get_users(self):
        return controller.get_users()

    # my code to comment
    def add(self, num1, num2):
        return controller.add(num1, num2)

    # my code to comment
    def sub(self, num1, num2):
        return controller.sub(num1, num2)

    # my code to comment
    def mul(self, num1, num2):
        return controller.mul(num1, num2)

    # my code to comment
    def div(self, num1, num2):
        return controller.div(num1, num2)

    def get_user_info(self, username):
        return controller.get_user_info(username)
