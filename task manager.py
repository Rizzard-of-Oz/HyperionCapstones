'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

# =====importing libraries===========
import datetime


# from importlib.resources import contents

# from macpath import split


def register_user():
    new_user_file = open('user.txt', 'r')
    user_data = []
    new_username = input("Enter your username: ").lower()
    new_password = input("Enter password: ").lower()
    passconfirm = input("Enter password again to confirm your new password: ").lower()

    for user in new_user_file:  # for loop to read line in the file
        user_new = user.split(", ")  # splitting the comma and the space
        user_data.append(user_new[0])
    print(user_data)

    on = True
    while on:
        if new_username in user_data:
            print("username already in use. Please enter new username")
            new_username = input("Enter username: ").lower()
        elif new_username not in user_data:
            print("New user added")
            on = False  # on is now false so it can break the loop when the details are correct

        new_user_file.close()
    while passconfirm != new_password:
        new_password = input("Enter password: ")
        passconfirm = input("Enter password again: ")

        if passconfirm == new_password:
            break

        print("You are logged in , welcome")  # user entered correct details

    with open('user.txt', 'a+') as add_user_file:
        add_user_file.write(f'\n{new_username}, {new_password}')


def add_task():
    add_user = input(" Enter username for task: ")
    tasktitle = input("Enter title of task: ")  # asks user for title of task
    description = input("Enter description of task: ")  # ask user to describe task
    duedate = input("Enter due date of task: ")  # asks user for due date
    task_complete = input("Task Complete?: Yes/No")
    task_date = datetime.today()  # prints current date
    task_date = task_date.strftime("%d,%b,%y")

    with open('tasks.txt', 'w') as f:
        # writes the info to the text file
        f.write(
            f"\n{add_user} +{tasktitle} + {description} + {duedate} +{task_complete} + {task_date},No")


def view_all():
    with open('tasks.txt', 'r') as task_file:
        task_info = task_file.readlines()
        task_counter = 0
        dict_tasks = {}

        for line in task_info:
            add_user, task_title, description, duedate, task_date, task_complete = line.split(", ")
            task_counter += 1
            dict_tasks[task_counter] = line.split('\n').split(', ')

            print(f''' Task assigned: {add_user}
                                        Task description: {description}
                                        Task due date:     {duedate}
                                        Task completed date: {task_date}
                                        Task  completed:        {task_complete}''')


def view_mine():
    with open('tasks.txt', 'r') as task_file:
        task_file.readlines()
        task_counter = 0
        dict_tasks = {}

        for line in task_file:
            add_user, task_title, description, duedate, task_date, task_complete = line.split(", ")
            task_counter += 1
            dict_tasks[task_counter] = line.split('\n').split(', ')

            print(f''' Task assigned: {add_user}
                                                   Task description: {description}
                                                   Task due date:     {duedate}
                                                   Task completed date: {task_date}
                                                   Task  completed:        {task_complete}''')

            task_content(dict_tasks)


def task_files(task_dict):
    while True:
        selecttask_index = input(
            "Enter the task number that you would like to view or -1 to go home: ")  # enter task number to select or -1 to exit
        if selecttask_index == -1:
            break

        marktask = input("Would you like mark task as complete or edit the task?: ").lower()

        if marktask == 'complete':
            selected_task.replace(selected_task[-1], "Yes\n")  # task will be marked complete with a yes

        elif marktask == 'edit':
            edit_task = input("Would you like to edit the task due date or change user?: ")
            if edit_task == 'user':
                update_username = input("Enter username: ").lower()
                task_dict[selected_task][0] = update_username

            elif edit_task == 'due date':
                date_edit = input("Enter date that you want to change")
                new_date = input("Enter new due date for task")

    print("\n".join([", ".join(t) for t in task_dict.values()]))
    with open('tasks.txt', 'w') as update_file:
        update_file.write("\n".join([", ".join(t) for t in task_dict.values()]))


def reports():
    print("Stats report: \n")
    with open("task_overview.txt", "w+") as task_overview:
        task_overview.write(lines)
        print(task_report())

    with open("user_overview.txt", "w+") as user_overview:
        user_overview.write(lines)
        print(user_report())


def task_report():
    dict_tasks = {}
    complete_task = 0
    incomplete_task = 0
    overduetask = 0
    total_user_tasks = 0

    with open('tasks.txt', 'r') as task_file:
        content = task_file.readlines()

        for line in content:
            total_user_tasks += 1
            dict_tasks[total_user_tasks] = line.strip('\n').split(", ")

        for line in content:
            task = line.strip('\n').split(", ")
            print(task)

            if task[-1].strip('\n') == "Yes":
                complete_task += 1

            elif task[-1].strip('\n') == "No":
                incomplete_task += 1

            date_check = datetime.strptime(task[-2], "%d %b %Y")

            if date_check < datetime.today() and "No" == task[-1].strip('\n'):
                overduetask += 1

            if len(dict_tasks) == 0:
                print("No tasks are in here")

            percent_incomplete = float(incomplete_task * 100 / len(dict_tasks))
            # percent_complete = float(complete_task * 100 / len(dict_tasks))
            percent_overdue = (overduetask * 100) / len(dict_tasks)

            with open('user_overview.txt', 'r+') as f_user:
                f_user.write(f'Total tasks created: {len(dict_tasks)} \n')
                f_user.write(f'Total tasks assigned to user : {total_user_tasks} \n ')

                f_user.write(f'Total tasks complete: {complete_task} \n ')
                f_user.write(f'Total percentage of tasks incomplete : {percent_incomplete}')
                f_user.write(f'Total percentage of overdue tasks: {percent_overdue}')


def user_report():
    dict_users = {}
    total_users = 0

    with open('user_overview.txt', 'w', encoding='utf-8') as user_overview:
        for new_user in dict_users:
            if new_user in dict_users or 'admin' in dict_users:
                total_users += 1
            else:
                break

    dict_tasks = {}
    total_task_users = 0
    total_tasks = 0

    with open('tasks.txt', 'r') as task_file:
        contents = task_file.readlines()
        total_tasks = len(dict_tasks)  # getting length of dictionary

        with open('user.txt', 'r') as user_file:
            user_info = user_file.readlines()
            total_task_users = len(user_info)  # getting total users in dictionary

            for line in user_info:
                username = line.split(", ")[0]
                completed_task = 0
                incompleted_task = 0
                overdue_task = 0
                specific_user_task = 0
                percent_incomplete = 0
                percent_complete = 0
                percent_overdue = 0

                for line in user_info:
                    task = line.strip('\n').split(", ")

                    if username == task[0]:
                        specific_user_task += 1

                        if task[-1].strip('\n') == "Yes":
                            completed_task += 1

                        elif task[-1].strip('\n') == "No":
                            incompleted_task += 1

                        date_check = datetime.strptime(task[-2], "%d %b %Y")

                        if date_check < datetime.today() and "No" == task[-1].strip('\n'):
                            overdue_task += 1

                    try:
                        if incompleted_task > 0:
                            percent_incomplete = (total_tasks / incompleted_task) * 100

                        if completed_task > 0:
                            percent_complete = (total_tasks / completed_task) * 100

                        if overdue_task > 0:
                            percent_overdue = (total_tasks / (incompleted_task + overdue_task)) * 100

                    except ZeroDivisionError:
                        pass

            with open('user_overview.txt', 'a+') as f_user:
                f_user.write(f'Total tasks created: {len(dict_tasks)} \n')
                f_user.write(f'Total tasks assigned to user : {username} : {specific_user_task} \n ')

                f_user.write(f'Total percentage of tasks complete: {percent_complete} \n ')
                f_user.write(f'Total percentage of tasks incomplete : {percent_incomplete}')
                f_user.write(f'Total percentage of overdue tasks: {percent_overdue}')


def display_num():
    task_counter = 0
    user_counter = 0

    with open('tasks.txt', 'r+') as task_file:  # opening task file to read and write
        for line in task_file:
            task_file.readline(int(line))
            task_counter += 1  # adds task  each time a new one is added
            print(f'Total tasks: {task_counter}')

    with open('user.txt', 'r+') as user_file:  # opening user file to read and write
        for line in user_file:
            user_file.readline(int(line))
            user_counter += 1  # adds user when one is added
            print(f'Total number of users: {user_counter}\n')


def menu():
    if username == 'admin':  # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    if menu == 'r':
        register_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'd':
        display_num()

    elif menu == 'gr':  # generate report
        task_report()
        user_report()


    elif menu == 'ds':  # edited menu option to display statistics
        reports()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


print("Enter login details: ")
read_file = open('user.txt', 'r+')  # opens and reads user.txt

user_data = []
password_list = []  # storing user data in lists

for data in read_file:
    list_data = data.strip('\n').split(", ")
    user_data.append(list_data[0])
    password_list.append(list_data[1].strip('\n'))

read_file.close()

username = input("Enter username: ").lower
while username not in user_data:  # checking if username is in the list
    print("Username not found please enter correct username")
    username = input("Enter username: ").lower()

password = input("Enter password: ")  # checking if password is in the list
while not (password_list[user_data.index(username)]) == password:
    print("Incorrect password")
    password = input("Enter password: ")

print("Login successful, welcome. ")

while True:
    menu()  # loads menu after logging and calling the function
