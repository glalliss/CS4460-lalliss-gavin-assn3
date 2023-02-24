# This module acts like the server. Queries come in as function calls and something is returned.
# You should probably have it return: numbers, strings, dictionaries, lists, or JSON.
# Let the client side change that into data objects if necessary.
import os
import bcrypt
import datetime


def login(user, password):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":")
        user_dict[user_info_list[0]] = user_info_list
    passwd.close()
    if user in user_dict:
        database_pw = user_dict.get(user)[1]
        database_pw = database_pw.encode('utf-8')
        hashed = bcrypt.hashpw(database_pw, bcrypt.gensalt())
        user_pw = password.encode('utf-8')
        if bcrypt.checkpw(user_pw, hashed):
            return user_dict.get(user)
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
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":")
        # if user_info matches username then create and return dictionary of personal info
        if username == user_info_list[0]:
            user_dict = {
                "username": user_info_list[0],
                "hashed_password": user_info_list[1],
                "employee_ID": user_info_list[2],
                "job_ID": user_info_list[3],
                "name": user_info_list[4],
                "email": user_info_list[5],
                "last_login": user_info_list[6],
             }
    passwd.close()
    return user_dict


def update_name(username, new_name):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if username == user_info_list[0]:
            passwd.write(user_info_list[0] + ":" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + f":{new_name}:" + user_info_list[5] + ":" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_username(old_username, new_username):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if old_username == user_info_list[0]:
            passwd.write(f"{new_username}:" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + ":" + user_info_list[4] + ":" + user_info_list[5] + ":" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_email(username, new_email):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if username == user_info_list[0]:
            passwd.write(user_info_list[0] + ":" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + ":" + user_info_list[4] + f":{new_email}:" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_password(username, new_password):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if username == user_info_list[0]:
            passwd.write(line.replace(user_info_list[1], new_password))
        else:
            passwd.write(line)
    passwd.close()


def update_login_timestamp(username):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if username == user_info_list[0]:
            passwd.write(line.replace(user_info_list[6], str(datetime.datetime.now())))
        else:
            passwd.write(line)
    passwd.close()
