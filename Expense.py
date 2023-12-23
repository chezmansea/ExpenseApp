import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount): # like insert into
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.updated_at = None
        self.created_at = datetime.utcnow()

    def update(self, title = None, amount = None): # like update table name (expenses) set col=val ......
        self.title = title if title is not None else self.title
        self.amount = amount if title is not None else self.amount
        self.updated_at = datetime.utcnow()

    def to_dict(self): # like select from table name ....
        expense_dictionary = {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None # if first record, leave updated at value to be None ie no changes
        }
        return expense_dictionary


if __name__ == '__main__':
    expense = Expense(title='Transportation', amount=20)

    # My expense yesterday
    print(expense.to_dict())

    # My expense for today
    todays_expense = Expense(title='Transportation', amount=50)

    print(todays_expense.to_dict())

    # My expense towards the end of the day
    expense.update(title = 'Updated Transportation', amount=150)
    print(expense.to_dict())