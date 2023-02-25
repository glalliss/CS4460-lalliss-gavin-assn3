# This module acts like the server. Queries come in as function calls and something is returned.
# You should probably have it return: numbers, strings, dictionaries, lists, or JSON.
# Let the client side change that into data objects if necessary.
import os
import bcrypt
import datetime


def login(user, password):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        user_dict[user_info_list[0]] = user_info_list
    passwd.close()
    if user in user_dict:
        database_pw = user_dict.get(user)[1]
        if database_pw == "73Mp()R@rY":
            return user_dict.get(user)
        database_pw = database_pw.encode('utf-8')
        hashed = bcrypt.hashpw(database_pw, bcrypt.gensalt())
        user_pw = password.encode('utf-8')
        if bcrypt.checkpw(user_pw, hashed):
            return user_dict.get(user)
    return -1


def add(num1, num2):
    return float(num1) + float(num2)


def sub(num1, num2):
    return float(num1) - float(num2)


def mul(num1, num2):
    return float(num1) * float(num2)


def div(num1, num2):
    return float(num1) / float(num2)


def get_users():
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        user_dict[f"{user_info_list[0]}"] = {
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


def get_managers():
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if user_info_list[2] == "1" or user_info_list[2] == "2":
            user_dict[f"{user_info_list[0]}"] = {
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


def get_user_info(employee_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        # if user_info matches username then create and return dictionary of personal info
        if employee_id == user_info_list[2]:
            user_dict = {
                "username": user_info_list[0],
                "hashed_password": user_info_list[1],
                "employee_ID": user_info_list[2],
                "job_ID": user_info_list[3],
                "name": user_info_list[4],
                "email": user_info_list[5],
                "last_login": user_info_list[6],
             }
            break
    passwd.close()
    return user_dict


def get_username(employee_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    passwd.close()
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if user_info_list[2] == employee_id:
            return user_info_list[0]


def new_employee_id():
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    last = 1
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if last == len(passwd_file):
            new_id = int(user_info_list[2]) + 1
        last += 1
    passwd.close()
    return new_id


def add_user(name, username, email, job_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd.readlines()
    passwd.write(f"{username}:73Mp()R@rY:{new_employee_id()}:{job_id}:{name}:{email}:never\n")
    passwd.close()


def update_name(employee_id, new_name):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(user_info_list[0] + ":" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + f":{new_name}:" + user_info_list[5] + ":" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_username(employee_id, new_username):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(f"{new_username}:" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + ":" + user_info_list[4] + ":" + user_info_list[5] + ":" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_email(employee_id, new_email):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(user_info_list[0] + ":" + user_info_list[1] + ":" + user_info_list[2] + ":" + user_info_list[3] + ":" + user_info_list[4] + f":{new_email}:" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()


def update_job_title(employee_id, new_job_title):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(user_info_list[0] + ":" + user_info_list[1] + ":" + user_info_list[2] + f":{new_job_title}:" + user_info_list[4] + ":" + user_info_list[5] + ":" + user_info_list[6] + "\n")
        else:
            passwd.write(line)
    passwd.close()
    pass


def remove_user(employee_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write("")
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


def update_login_timestamp(employee_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(line.replace(user_info_list[6], str(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))))
        else:
            passwd.write(line)
    passwd.close()


def update_calculations(employee_id, result, calc_type):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    calc_dir = os.path.dirname(__file__).replace("controller", "data")
    calc_file_path = os.path.join(calc_dir, "calcs.txt")
    calc = open(calc_file_path, 'r+')
    calc.readlines()
    calc.write(f"{date_time}<>{employee_id}<>{result}<>{calc_type}\n")
    calc.close()


def populate_calculations(filter_dict):
    calc_dir = os.path.dirname(__file__).replace("controller", "data")
    calc_file_path = os.path.join(calc_dir, "calcs.txt")
    calc = open(calc_file_path, 'r')
    calc_file = calc.readlines()
    calc.close()
    calc_dict = {}
    for line in calc_file:
        calc_info_list = line.replace("\n", "").split("<>", 3)
        if filter_dict.get(calc_info_list[3]):
            calc_dict[calc_info_list[0]] = calc_info_list
    return calc_dict
