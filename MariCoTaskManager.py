#Description: Build an online task management system that allows users to create, view, update, and delete tasks. The system should provide features like task prioritization, due dates, status updates, and error handling for input validation.
"""
Pseudo Code:
1. Define a Task class with attributes: title, description, due date, priority, and status.
2. Implement error handling for input validation (e.g., ensuring the due date is a valid date, priority is within a valid range, etc.).
3. Create a TaskManager class to manage tasks:
o Initialize an empty list to store tasks. • Implement methods to add_task, update_task, delete_task, and view_tasks.
o Allow users to input task details and handle errors appropriately.
4. Utilize Object-Oriented Programming (OOP) concepts to encapsulate data and logic within classes and methods.
5. Develop a user interface for interaction, displaying options like create task, update task, view tasks, and delete task.
"""
import datetime         # Importing the required modules

class Task:
    def __init__(self, title, description, due_date, priority):   # Defining a Task class with attributes: title, description, due date, priority, and status.
        self.title = title
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = 'status'

class TaskManager():            #Creating task manager class to add tasks, update tasks, view tasks, delete tasks and exit program
    def __init__(self):
        self.tasks = []         # Initializing an empty list to store tasks.

    def add_task(self, task):
        self.tasks.append(task)  #Add task

    def update_task(self, task_idx, new_title, new_description, new_due_date, new_priority): #Update task
        task = self.tasks[task_idx]
        task.title = new_title
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority

    def delete_task(self, task_idx):            #delete tasks using task id
        del self.tasks[task_idx]

    def view_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"Task {idx + 1}:")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due Date: {task.due_date}")
            print(f"Priority: {task.priority}")
            print(f"Status: {task.status}")
            print("=" * 20)

def validate_date(date_string):     # Function to validate the due date
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')     #using the import module to format date for validation
        return True
    except ValueError:
        return False

def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager Menu:")
        print("1. Create Task")
        print("2. Update Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = int(input("Enter priority (1-5): "))

            if validate_date(due_date) and 1 <= priority <= 5:
                task = Task(title, description, due_date, priority)
                task_manager.add_task(task)
            else:
                print("Invalid input. Task not added.")

        elif choice == "2":
            task_manager.view_tasks()
            task_idx = int(input("Enter task number to update: ")) 

            if 0 <= task_idx < len(task_manager.tasks):
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                new_priority = int(input("Enter new priority (1-5): "))

                if validate_date(new_due_date) and 1 <= new_priority <= 5:
                    task_manager.update_task(task_idx, new_title, new_description, new_due_date, new_priority)
                    print("Task updated.")
                else:
                    print("Invalid input. Task not updated.")
            else:
                print("Invalid task number.")

        elif choice == "3":
            task_manager.view_tasks()

        elif choice == "4":
            task_manager.view_tasks()
            task_idx = int(input("Enter task number to delete: "))   #Deleting tasks using task id

            if 0 <= task_idx < len(task_manager.tasks):
                task_manager.delete_task(task_idx)
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Exiting the program.")

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()