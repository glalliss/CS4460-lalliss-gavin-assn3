install bcrypt if not already installed

### app.py
* Begins the program from Login.py

### api.py
* works like a communicator between server and client to perform functions

### Login.py
* Creates API() to communicate with server
* Creates GUI with title being "Login"
* Options
  * Login option with 2 inputs for username and password
    * If successful login then switch_menu(mm, back_button) 
    * else set_display("Invalid username or Password") 
  * Demo-option with 2 inputs for 2 things to add together as a float
    * inputing 2 numbers results in addition being shown
    * else error that doesn't stop the program
  * Exit option exits program

### MainMenu.py
* Creates GUI with title being "User: {username}"
* Options
  * Example checklist/filtering
    * switch_menu(check)
    * creates a new instance of class every time which can be used to check access authorization every time
  * Example IO
    * enter number to get that many inputs (add check to make sure it's not too high to display)
    * transition from __io to __io1 to get inputs and display/print inputs after submitted
  * Manage Users
    * switch_menu(mu)
  * Back

### Checklist.py
* contains list of words when initialized that are then shuffled then printed
* Options
  * filter words starting with ...
  * Back

### ManageUsers.py
* Creates API() to communicate with "server" then populates users
* get users from api (check text file rather than just a hard coded string)
  * add_option for each user with the possibility to edit_user
  * use process_edit to actually update server information with new info

### Menu.py
* has all of the functions/methods for anything to do with the gui menus

### controller.py
* communication is from client page to api to controller then from controller to api to client page

## How to Run Program
* Just run the file app.py
* login info
* etc.

# DON'T FORGET TO DO report.pdf!