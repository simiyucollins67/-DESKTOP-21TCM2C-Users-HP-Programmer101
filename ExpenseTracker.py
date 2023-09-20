class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float (amount)
        self.category = category
        self.date = date 
        self.description = description
class Category(Expense): 
        pass                #Represent different expense categories 
class ExpenseTracker: 
     def __init__(self, records):
        self.records = records              
        records = []                         #Manage expenses 
     def add_expense():
          pass
     def view_expenses_by_category():
          pass
     def generate_report():
          pass
                             
