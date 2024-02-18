#==== Capstone project ====

#=====Importing libraries===========
'''This is the section where libraries are imported'''
from datetime import datetime

#====Login Section====
'''This section deals with code that allows a user to login
    - Usernames and password are read from the user.txt file
    - A dictionary is used to store user credentials from the user.txt file
    - A while loop and user function are used to validate the login.
'''
# Intialise variables
user_list = []
password_list = []
task_count = 0
user_count = 0
login_status = False
date_format = '%d %b %Y'

# ================== User Defined Functions ================== #
# ____________________________________________________________ #

# Set up a login verification function that returns login status stored in a boolean variable login_s
# Checks that the username is in the dictionary, and that the password matches the username key
# Displays appropriate error messages at each step if conditions are not met
def login_verify(u_name, p_word, dict_credentials):
    if u_name in dict_credentials:
        if p_word == dict_credentials[u_name]:
            return True
        else:
            print('Invalid password')
    else:
        print('Invalid username')
        return False

def reg_user():
    # Code to register a new user and add them to user.txt
    # Check if the username already exists and if so, do not register, and display message
    # Check to see if the password and confirmed passwords match, 
    # and then write the username and password to file if they do
    username = input("Please enter new user to register: ")
    if username in user_list:
        print("Sorry, that user already exists")
    else:
        new_password = input('Please enter a new password: ')
        confirm_password = input('Please confirm password: ')
        if new_password == confirm_password:
            with open('user.txt','a') as file:
                file.write(f'\n{username}, {new_password}')
        else:
            print('The password does not match, please try again')


def add_task():
    # Code to add a new task to tasks.txt
    # Promp user for task details and append them to task file
    username = input('Please enter the username: ')
    task_title = input('Please enter the title of the task: ')
    task_description = input('Please enter a task description: ')
    task_due_date = input('Please enter the due date of the task (%d %b %Y format e.g. 01 Jan 2000): ')
    task_assign_date = datetime.now().date().strftime(date_format)
    task_complete = "No"
    with open('tasks.txt','a') as file:
        file.write(f'\n{username}, {task_title}, {task_description}, {task_assign_date}, {task_due_date}, {task_complete}\n')

def view_all():
    # Code to view all tasks listed in 'tasks.txt' in an easy-to-read manner
    with open('tasks.txt','r+') as file:
            for line in file:
                l_list = line.split(', ')
                print(f'''__________________________________________________________________________________ \n\n
                       Task: \t {l_list[1]}\n
                       Assigned to: \t {l_list[0]}\n
                       Date Assigned: \t {l_list[3]}\n
                       Due Date: \t {l_list[4]}\n
                       Task Complete: \t {l_list[5]}\n
                       Task Description: \n\t\t {l_list[2]}\n\n
__________________________________________________________________________________ \n\n
                      ''')
    


def view_mine(username):
    # Code to view all tasks assigned to the current user
    # Display tasks with corresponding numbers for identification
    # Allow the user to select a specific task (by entering a number)
    # If the user selects a specific task, provide options to mark the task as complete or edit the task
    
    # Display all tasks in predetermined format
    with open('tasks.txt','r+') as file:
        for line in file:
            l_list = line.split(', ')
            counter = 0
            if l_list[0] == username:
                counter += 1
                print(f'''_________________________________________________________________ \n\n
                       Task number: \t {counter}\n
                       Task: \t {l_list[1]}\n
                       Assigned to: \t {l_list[0]}\n
                       Date Assigned: \t {l_list[3]}\n
                       Due Date: \t {l_list[4]}\n
                       Task Complete: \t {l_list[5]}\n
                       Task Description: \n {l_list[2]}\n\n
                       _________________________________________________________________ \n\n
                      ''')

    # Prompt user to select a task number            
    try:
        t_number = int(input('Please chose a task number to edit (-1 to exit to main menu): '))
    except ValueError:
        print('Please enter a valid number')

    if (t_number > 0) and (t_number <= counter):
        option = input('''Please select if you wish to edit or mark this task complete \n
                   m - \t Mark task as complete\n
                   e - \t Edit task\n
                   c - \t Cancel\n
                   ''')

        # Call function to mark complete or edit
        if option == 'm':
            mark_task_complete(t_number,username)
        elif option == 'e':
            edit_task(t_number,username)
        elif option == 'c':
            pass
        else:
            print('Please enter a valid option.')
    
    # Return to menu if -1 is selected
    elif t_number == -1:
        if admin_status == True:
            menu = input('''Select one of the following Options below:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - View my task(s)
                        ds - Statistics
                        e - Exit
                        : ''').lower()
        else:
            menu = input('''Select one of the following Options below:
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        e - Exit
                        : ''').lower()
    else:
        print('Please enter a valid task number')



def mark_task_complete(task_num, username):
    # Code to mark the task with the given task number as complete in 'tasks.txt'
    counter = 0
    with open('tasks.txt','r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            l_list = line.split(', ')
            if l_list[0] == username:
                counter += 1
                if counter == task_num:
                    lines[i] = f'{l_list[0]}, {l_list[1]}, {l_list[2]}, {l_list[3]}, {l_list[4]}, "Yes"\n'
    
    # Rewrite tasks.txt with modified temp file
    with open('tasks.txt', 'w') as file:
        file.writelines(lines)


            

def edit_task(task_num, edit_field):
    # Edit the task with the given task number in 'tasks.txt'
    # Allow editing of the username or the due date of the task
    # The task can only be edited if it has not yet been completed    
    counter = 0
    with open('tasks.txt','r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            l_list = line.split(', ')
            if l_list[0] == username:
                counter += 1
                if counter == task_num and l_list[5].lower() != 'yes':
                    if edit_field == 'u':
                        new_username = input('Please provide new username: ')
                        lines[i] = f'{new_username}, {l_list[1]}, {l_list[2]}, {l_list[3]}, {l_list[4]}, {l_list[5]}\n'
                    elif edit_field == 'd':
                        new_due_date = input('Please provide new due date: ')
                        lines[i] = f'{l_list[0]}, {l_list[1]}, {l_list[2]}, {l_list[3]}, {new_due_date}, {l_list[5]}\n'
                    else:
                        print("Please select valid option.")
    
    with open('tasks.txt', 'w') as file:
        file.writelines(lines)

def display_statistics():
    # Calculate the statistics, calculate the total number of users, and the total number of tasks,
    # and display the statistics after tallying
    task_count = 0
    user_count = 0
    with open('tasks.txt','r+') as file:
        for line in file:
            task_count += 1

    with open('user.txt','r+') as file:
        for line in file:
            user_count += 1
    
    print(f'The number of users is {user_count} and the number of tasks is {task_count}')

def generate_reports():
    # ****** Generate reports based on user.txt and tasks.txt ****** 
    with open('tasks.txt','r+') as task_file:
            task_lines = task_file.readlines()

    with open('user.txt','r+') as user_file:
        user_lines = user_file.readlines()

    # Generate reports on total tasks for all users
    # tasks complete tasks
    # tasks incomplete and percentage of total 
    # tasks overdue and percentage of total

    total_tasks = len(task_lines)
    total_users = len(user_lines)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    for task_line in task_lines:
        task_data = task_line.strip().split(', ')
        if task_data[5] == 'No':
            uncompleted_tasks += 1
            due_date = datetime.strptime(task_data[4], date_format)
            if due_date < datetime.today():
                overdue_tasks += 1
        else:
            completed_tasks += 1

        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100

        task_report = f'''_________________________________________________________________ \n\n
Task Overview:
Total tasks: \t {total_tasks}
Completed tasks: \t {completed_tasks}
Uncompleted tasks: \t {uncompleted_tasks}
Tasks not completed and overdue: \t {overdue_tasks}
Percentage of tasks incomplete: \t {incomplete_percentage:.2f}%
Percentage of tasks overdue: \t {overdue_percentage:.2f}%
_________________________________________________________________ \n\n
'''

        with open('task_overview.txt', 'w+') as task_overview_file:
            task_overview_file.write(task_report)

    user_stats = []

    # Generate stats for users, total tasks assigned to a single user, 
    # tasks complete and percentage of total 
    # tasks incomplete and percentage of total 
    # tasks overdue and percentage of total 
    # write to user_overview.txt

    for user_line in user_lines:
        user_data = user_line.strip().split(', ')
        user_task_count = 0
        user_uncompleted_tasks = 0
        user_overdue_tasks = 0
        user_completed_tasks = 0
        
        for task_line in task_lines:            
            task_data = task_line.strip().split(', ')
            if user_data[0] == task_data[0]:
                # increase counter for tasks
                user_task_count += 1
                if task_data[5] == 'No':
                    user_uncompleted_tasks += 1
                    due_date = datetime.strptime(task_data[4], date_format)
                    if due_date < datetime.today():
                        user_overdue_tasks += 1
                else:
                    user_completed_tasks += 1

        # avoiding div by 0 error                    
        if user_task_count > 0:
            percentage_total_tasks = (user_task_count/ total_tasks)
            complete_percentage = (user_completed_tasks / user_task_count) * 100
            incomplete_percentage = (user_uncompleted_tasks / user_task_count) * 100
            overdue_percentage = (user_overdue_tasks / user_task_count) * 100
        else:
            # Set percentages to 0 if there are no tasks for the user
            percentage_total_tasks = 0
            complete_percentage = 0
            incomplete_percentage = 0
            overdue_percentage = 0

        user_tuple = (user_data[0], user_task_count, percentage_total_tasks, 
                      complete_percentage, incomplete_percentage, overdue_percentage)
        user_stats.append(user_tuple)

    user_overview = f'''User Overview:
    Total users: {total_users}
    Total tasks: {total_tasks} \n
'''
    
    for stat_line in user_stats:
        user_overview = user_overview + f'''
    Username: \t {stat_line[0]}
    Number of tasks: \t {stat_line[1]}
    Percentage total tasks: \t {stat_line[2]}
    Percentage of tasks complete: \t {stat_line[3]}
    Percentage of tasks incomplete: \t {stat_line[4]}
    Percentage of tasks overdue: \t {stat_line[5]}
        '''

    with open('user_overview.txt', 'w+') as user_overview_file:
        user_overview_file.write(user_overview)


# ================== Main Code Block ================== #
# ____________________________________________________________ #  

# Open the user.txt file, and add the usernames to a list, as well as the associated passwords
with open('user.txt','r+') as file:
    for line in file:
        line_split_list = line.strip().split(', ')
        user_list.append(line_split_list[0])
        password_list.append(line_split_list[1])

# Using the dict and zip functions, combine the two lists into a dictionary called credentials,
# this dictionary will be used for login verification
credentials = dict(zip(user_list, password_list))

# Prompt the user to enter a username and password for a login attempt,
# verify the information entered against the credentials dictionary,
# if either username or password don't match, display the relevant error message
try:
    username = input('Please enter a username: ')
    password = input('Please enter a password: ')
except ValueError:
    print('Please enter a valid input')

# Verify the login            
login_status = login_verify(username, password, credentials)

print(login_status)

# While the user isn't logged in, keep prompting the user to enter their credentials  
while login_status == False:
    try:
        username = input('Please enter a username: ')
        password = input('Please enter a password: ')
    except ValueError:
        print('Please enter a valid input')
    login_verify(username, password, credentials)

# If the login is successful and the username is 'admin', set admin status to true
if username == 'admin':
    admin_status = True
else:
    admin_status = False


#==== Control panel after login ====

while login_status == True:
    # Present the menu to the user, admin menu and user menu is different
    # make sure that the user input is coneverted to lower case.
    if admin_status == True:
        menu = input('''Select one of the following Options below:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - View my task(s)
                        ds - Statistics
                        gr - Generate reports
                        e - Exit
                        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        e - Exit
                        : ''').lower()


    if (menu == 'r') and (admin_status == True):
        ''' - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise present an error message.'''
        # Call reg_user function for the functionality above
        reg_user()


    elif menu == 'a':
        '''- Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Get the current date.
            - Add the data to the file tasks.txt and
            - Add 'No' for task completion status, because of new task.'''
        # Call add_task function for functionality above
        add_task()
        

    elif menu == 'va':
        # Display all tasks in the tasks.txt file in a specified format
        ''' - Read a line from the file.
            - Split that line where there is comma and space.
            - Print the results in the format shown in the Output 2 in L1T19 pdf
        '''
        # Call view_all() function for functionality above
        view_all()
                

    elif menu == 'vm':
        # Read tasks from the tasks.txt file, and display the task if it belongs to the current logged in user
        ''' - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        view_mine(username)

    elif (menu == 'ds') and (admin_status == True):
        '''Calculate the statistics, calculate the total number of users, and the total number of tasks,
        and display them after tallying'''
        display_statistics()
        

    elif (menu == 'gr') and (admin_status == True):
        '''Call the generate reports function to generate reports to 
        task_overview.txt and user_overview.txt'''
        generate_reports()    


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print('You have made a wrong choice, Please Try again')

#==== Capstone project ====


# ****************** End of code ********************* #