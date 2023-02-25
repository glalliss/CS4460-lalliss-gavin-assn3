# This module acts like the server. Queries come in as function calls and something is returned.
# You should probably have it return: numbers, strings, dictionaries, lists, or JSON.
# Let the client side change that into data objects if necessary.
import os
import bcrypt
import datetime


# login
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
        # temporary password so return dictionary of the users data
        if database_pw == "73Mp()R@rY":
            return user_dict.get(user)
        # log login
        log(user_dict.get(user)[2], "logged in")
        database_pw = database_pw.encode('utf-8')
        hashed = bcrypt.hashpw(database_pw, bcrypt.gensalt())
        user_pw = password.encode('utf-8')
        # compare encrypted passwords
        if bcrypt.checkpw(user_pw, hashed):
            return user_dict.get(user)
    # return -1 if failed login
    return -1


# calculations for addition, subtraction, multiplication, and division performed and result returned
def add(num1, num2):
    return float(num1) + float(num2)


def sub(num1, num2):
    return float(num1) - float(num2)


def mul(num1, num2):
    return float(num1) * float(num2)


def div(num1, num2):
    return float(num1) / float(num2)


# return dictionary of dictionaries of all users with keyword of employee_id to differentiate between users
def get_users(performer):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        user_dict[f"{user_info_list[2]}"] = {
            "username": user_info_list[0],
            "hashed_password": user_info_list[1],
            "employee_ID": user_info_list[2],
            "job_ID": user_info_list[3],
            "name": user_info_list[4],
            "email": user_info_list[5],
            "last_login": user_info_list[6],
        }
    passwd.close()
    # log because only used when viewing human resources page
    log(performer, "viewed human resources page")
    return user_dict


# similar to get_users above but only returns admin and human resource account information
def get_managers(performer):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if user_info_list[3] == "1" or user_info_list[3] == "2":
            user_dict[f"{user_info_list[2]}"] = {
                "username": user_info_list[0],
                "hashed_password": user_info_list[1],
                "employee_ID": user_info_list[2],
                "job_ID": user_info_list[3],
                "name": user_info_list[4],
                "email": user_info_list[5],
                "last_login": user_info_list[6],
        }
    passwd.close()
    # log because only used when viewing admin page
    log(performer, "viewed admin page")
    return user_dict


# this is used for checking every access by returning a dictionary of your info
def get_personal_access_info(employee_id):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
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


# used to get info for another account or your own for editing purposes
def get_user_info(employee_id, performer):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r')
    passwd_file = passwd.readlines()
    user_dict = {}
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
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
    # log when viewing personal data that can also be edited
    log(performer, f"viewed {employee_id}'s personal info")
    return user_dict


# used for calculation page to show the username of who performed the application even if they change their username
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


# computes the next employee id based on the most recent issued that is still in use
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


# creates a new user by adding their information to the password file
def add_user(name, username, email, job_id, performer):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd.readlines()
    new_id = new_employee_id()
    passwd.write(f"{username}:73Mp()R@rY:{new_id}:{job_id}:{name}:{email}:never\n")
    passwd.close()
    # log who added the user and who the new user is
    log(performer, f"added {new_id} as a user")


# The following update_ methods are used to update the password file and log that there was a change as well
def update_name(employee_id, new_name, performer):
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
    log(performer, f"updated {employee_id}'s name")


def update_username(employee_id, new_username, performer):
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
    log(performer, f"updated {employee_id}'s username")


def update_email(employee_id, new_email, performer):
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
    log(performer, f"updated {employee_id}'s email")


def update_job_title(employee_id, new_job_title, performer):
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
    log(performer, f"updated {employee_id}'s job title to {new_job_title}")


# remove a user and log who removed them but only noting down employee_id
def remove_user(employee_id, performer):
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
    log(performer, f"removed {employee_id}")


# used for changing your password when your account is first created
def update_password(employee_id, new_password):
    password_dir = os.path.dirname(__file__).replace("controller", "data")
    password_file_path = os.path.join(password_dir, "passwd.txt")
    passwd = open(password_file_path, 'r+')
    passwd_file = passwd.readlines()
    passwd.close()
    passwd = open(password_file_path, 'w')
    for line in passwd_file:
        user_info_list = line.replace("\n", "").split(":", 6)
        if employee_id == user_info_list[2]:
            passwd.write(line.replace(user_info_list[1], new_password))
        else:
            passwd.write(line)
    passwd.close()


# updates login timestamp in the password file
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


# updates the calc file with the necessary information and logs what type of calculation was performed
def update_calculations(employee_id, result, calc_type):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    calc_dir = os.path.dirname(__file__).replace("controller", "data")
    calc_file_path = os.path.join(calc_dir, "calcs.txt")
    calc = open(calc_file_path, 'r+')
    calc.readlines()
    calc.write(f"{date_time}<>{employee_id}<>{result}<>{calc_type}\n")
    calc.close()
    calc_dict = {
        "1": "Addition",
        "2": "Subtraction",
        "3": "Multiplication",
        "4": "Division",
    }
    log(employee_id, f"performed {calc_dict[f'{calc_type}']}")


# used to create the list of calculations for the admin to view
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


# logs that the admin viewed the calculation history
def log_calculation_page(employee_id):
    log(employee_id, "viewed calculation history")


# method for writing the log of operations requesting who performed the operation and what they did
def log(employee_id, operation):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    log_dir = os.path.dirname(__file__).replace("controller", "data")
    log_file_path = os.path.join(log_dir, "logs.txt")
    log = open(log_file_path, 'r+')
    log.readlines()
    log.write(f"{date_time}<>{employee_id}<>{operation}\n")
    log.close()
