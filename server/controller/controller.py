# This module acts like the server. Queries come in as function calls and something is returned.
# You should probably have it return: numbers, strings, dictionaries, lists, or JSON.
# Let the client side change that into data objects if necessary.
import os
import bcrypt

# This variable is just for this demo
name = ""


def login(user, password):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":")
        print(user_info_list)
        print(len(user_info_list))
    passwd.close()
    # if this code is still here when you submit you will get an F and a public flogging
    if password == "password":
        global name
        name = user
        return 123456
    else:
        return -1


def get_users():
    return "Alice Bob Charlie Denise"


def add(num1, num2):
    return float(num1) + float(num2)


def sub(num1, num2):
    return float(num1) - float(num2)


def mul(num1, num2):
    return float(num1) * float(num2)


def div(num1, num2):
    return float(num1) / float(num2)


def get_user_info(username):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":")
        # if user_info matches username then create and return dictionary of personal info
        if username == user_info_list[0]:
            return {
                "username": user_info_list[0],
                "hashed_password": user_info_list[1],
                "employee_ID": user_info_list[2],
                "job_ID": user_info_list[3],
                "name": user_info_list[4],
                "email": user_info_list[5],
                "last_login": user_info_list[6],
             }
    passwd.close()

