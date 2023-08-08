# This is a task manager program that allows users to add, complete, delete, and display tasks.
# The data structure used to represent tasks is a dictionary with the following keys:
# title: The title of the task
# description: A description of the task
# completed: A boolean value indicating whether the task has been completed
# The program first creates an empty list to store tasks. It then defines four functions to add, complete, delete, and display tasks.
# The add_task function prompts the user for the title and description of a new task and then adds it to the task list.
# The complete_task function marks the task at the specified index as completed.
# The delete_task function deletes the task at the specified index from the task list.
# The display_tasks function displays all tasks in the task list.
# The main program loop displays the task manager menu and prompts the user to select an option. The user can then choose to add, complete, delete, or display tasks. The program quits when the user chooses to quit.

#empty list to store tasks
task_list = []

#function to add a new task to the list
def add_task(title, description):
    task = {
        "title:": title,
        "description": description,
        "completed": False
    }
    task_list.append(task)

    choice = input("Would you like to add another task? (y/n): ")
    if choice == "y":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    else:
        return
    
    print("\nTask added successfully.")

#function to mark a task as completed
def complete_task(task_index):
    task_list[task_index]["completed"] = True

    print("\nTask marked as completed.")

#function to delete a task
def delete_task(task_index):
    task_list.pop(task_index)

    print("\nTask deleted successfully.")

#function to display all tasks
def display_tasks():
    print("**********")
    for index in range(0, len(task_list)):
        print(f"{index} - {task_list[index]}")
    print("**********")

#main program loop
while True:
    print("\nTask Manager Menu:")
    print("1 - Add Task")
    print("2 - Complete Task")
    print("3 - Delete Tasks")
    print("4 - Display Tasks")
    print("Q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == "2":
        display_tasks()
        task_index = int(input("Enter the task index to complete: "))
        complete_task(task_index)
    elif choice == "3":
        display_tasks()
        task_index = int(input("Enter the task index to delete: "))
        delete_task(task_index)
    elif choice == "4":
        display_tasks()
    elif choice == "Q" or choice == "q":
        print("Thank you for using Task Manager, Goodbye!")
        break
    else:
        print("Invalid Choice, try again")