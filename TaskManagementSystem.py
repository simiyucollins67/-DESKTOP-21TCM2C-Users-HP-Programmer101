#Define a task class with the attributes title, description, due_date, priority, status
from datetime import datetime


class marico_task_manager:
    def __init__(self, title,description, due_date, priority, status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.priority=priority
        self.status=status
#Implementing error handling for input validation e.g due_date
#function to validate due_date
from datetime import datetime
def validate_due_date(self, due_date):
#initializing format
    format= '%d-%m-%y'
    try:
        datetime.date.time.strptime (due_date,format)
        return True
    except:
        ValueError
        return False
#function to validate the priority
def validate_priority (self, priority):
    if priority in range (1,5):
        return True
    else:
        return False
#creating task manager class
class Taskmanager:
#initializing an empty list
    def __init__ (self):
        self.tasks=[]
#implementing methods to add_task, view_task, updtate_task, delete_task
#function to add a task
    def add_task(self, tasks):
        self.tasks.append(tasks)
#function to update a task
    def update_task(self, tasks):
        for i in range(len(self.tasks)):
            if self.tasks[i].title==tasks.title:
                self.tasks[i]=tasks
                break
#function to delete task
    def delete_task(self, tasks):
        for i in range (len(self.tasks)):
            if self.tasks[i].title==tasks.title:
                del self.tasks[i]
                break
#Functions to view task
    def view_task(self):
        for task in self.tasks:
            print ('title:' , self.title)
            print ('description:' , self.description)
            print ('due_date:' , self.due_date)
            print ('priority:' , self.priority)
            print ('status:' , self.status)
            print('')
#Error handing in taskmanager: Allow user to input task & handle errors appropriately
def main():
    task_manager=Taskmanager()
    while True:
        print('1. create task')
        print('2. view task')
        print('3. update task')
        print('4. delete task')
        print('5. exit')
        choice=input('Enter your choice:')
        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            while not task.validate_due_date(task, due_date):
                due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            priority = int(input("Enter the priority of the task (1-5): "))
            while not task.validate_priority(task, priority):
                priority = int(input("Enter the priority of the task (1-5): "))
            status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            while not task.validate_status(task, status):
                status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            task = task(title, description, due_date, priority, status)
            task_manager.add_task(task)
        elif choice == "2":
            title = input("Enter the title of the task to be updated: ")
            description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            while not task.validate_due_date(task, due_date):
                due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            priority = int(input("Enter the priority of the task (1-5): "))
            while not task.validate_priority(task, priority):
                priority = int(input("Enter the priority of the task (1-5): "))
            status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            while not task.validate_status(task, status):
                status = input("Enter the status of the task (Not Started, In Progress, Completed): ")
            task = task(title, description, due_date, priority, status)
            task_manager.update_task(task)
        elif choice == "3":
            title = input("Enter the title of the task to be deleted: ")
            task = task(title, None)
        elif choice == "4":
            del task
        else: 
            exit ()        
        


    
        















    

    
    
