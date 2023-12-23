class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        for singleExpense in self.expenses:
            if singleExpense['id'] == expense_id:
                self.expenses.remove(singleExpense)
                break

    def get_expense_by_id(self, expense_id):
        for singleExpense in self.expenses:
            if singleExpense['id'] == expense_id:
                return singleExpense
        return None # return nothing ie - nothing is found
    #

    def get_expense_by_title(self, title):
        for singleExpense in self.expenses:
            if singleExpense['title'] == title:
                return singleExpense
        return None # return nothing ie - nothing is found

    def to_dict(self):
        expense_container = []
        for expense in self.expenses:
            expense_dictionary = {
                'id': expense['id'],
                'title': expense['title'],
                'amount': expense['amount']
            }
            expense_container.append(expense_dictionary)
        return expense_container

if __name__ == '__main__':

    # instantiate the ExpenseDatabase class for reusability
    expense_database = ExpenseDatabase()

    expense_database.add_expense({'id': 'randomId1', 'title': 'Healthcare', 'amount': 100})
    expense_database.add_expense({'id': 'randomId2', 'title': 'Furniture', 'amount': 400})
    expense_database.add_expense({'id': 'randomId3', 'title': 'Sportwear', 'amount': 600})

    # Lets see the default state of our expenses
    print('Default state of expense database:')
    print(expense_database.to_dict())

    # Lets remove an expense by a specific id - randomId2
    expense_database.remove_expense('randomId2')
    print(expense_database.to_dict())

    # Lets get an expense by id - third expense with id=randomId3
    print(expense_database.get_expense_by_id('randomId3'))

    # Lets get an expense by title field
    print(expense_database.get_expense_by_title('Healthcare'))