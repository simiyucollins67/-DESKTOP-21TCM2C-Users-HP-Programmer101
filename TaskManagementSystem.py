from datetime import datetime
class marico_task_manager:
    def __init__(self, title,description, due_date, priority, status): #Define a task class with the attributes title, description, due_date, priority, status
        self.title=title
        self.description=description
        self.due_date=due_date
        self.priority=priority
        self.status=status
    def validate_due_date(self, due_date):#Implementing error handling for input validation i.e. due_date attribute
        format= '%d-%m-%y' #initializing format
        try:
            datetime.strptime (due_date,format)
            return True
        except ValueError: 
            return False
    def validate_priority (self, priority): #Implementing error handling for input validation i.e. priority attribute 
            if priority in range (1,5): #function to validate the priority
                return True
            else:
                return False

        


    
        















    

    
    
