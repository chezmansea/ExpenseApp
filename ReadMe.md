# Welcome.

## Project Description

     Overview

        This project aims at keeping track of expenses using Object Oriented Programming in Python.

**To keep track of an expense, I have:**

1. Defined an expense class that holds the relevant attributes to store an expense.
2. In the expense class, I have created three methods which helps in updating (`update()` method) and retrieving (`to_dict()` method) the default values of the expenses.
3. The expense class uses the built-in python magic function (`__init__`) to initialise the default state of the expense values such as id, title, amount and the timestamps (created and updated at columns)

## How to clone this project:

1. In your terminal, copy and paste this: `git clone https://github.com/chezmansea/ExpenseApp.git`
2. cd into the cloned project - `cd ExpenseApp`
3. In this folder, you will see the list of the two classes (`Expense.py` and `ExpenseDatabase.py`)

## How to run this project

1. In your terminal, copy and paste this: `git clone https://github.com/chezmansea/ExpenseApp.git`
2. cd into the cloned project - `cd ExpenseApp`
3. In this folder, you will see the list of the two classes (`Expense.py` and `ExpenseDatabase.py`)
4. To execute and to see the result of Expense.py class, run `python Expense.py`
5. Three expense objects are expected as the result: 

**Prints first expense added to the Expense class when instantiating it - I called the to_dict method on the expense object to achieve this after instantiating expense**

`{'id': UUID('d62cde79-d60e-4f7a-9cd1-237f68a2dcef'), 'title': 'Transportation', 'amount': 20, 'created_at': '2023-12-23T21:48:38.237265', 'updated_at': None}`

**Prints second expense added to the Expense class when instantiating it**

`{'id': UUID('2699d860-e79a-4c22-93d6-c016fedb15d8'), 'title': 'Transportation', 'amount': 50, 'created_at': '2023-12-23T21:48:38.237580', 'updated_at': None}`

**Prints updated version of the expense when the update method is called on the expense object**

`{'id': UUID('d62cde79-d60e-4f7a-9cd1-237f68a2dcef'), 'title': 'Updated Transportation', 'amount': 150, 'created_at': '2023-12-23T21:48:38.237265', 'updated_at': '2023-12-23T21:48:38.237590'}`

6. To execute and to see the result of ExpenseDatabase.py class, run `python ExpenseDatabase.py`
7. Expected result for the ExpenseDatabase.py class:

**This values are the initial expense values that I used when instantiating the ExpenseDatabase class**
`[{'id': 'randomId1', 'title': 'Healthcare', 'amount': 100}, {'id': 'randomId2', 'title': 'Furniture', 'amount': 400}, {'id': 'randomId3', 'title': 'Sportwear', 'amount': 600}]`

**When I removed the second expense with id 'randomId2', I can see and confirm that the expense with the id (randomId2), is no longer in the list of the expenses**
`[{'id': 'randomId1', 'title': 'Healthcare', 'amount': 100}, {'id': 'randomId3', 'title': 'Sportwear', 'amount': 600}]`

**When I tried retrieving an expense with the id of 'randomId2', I am able to retrieve its exact object. What this means is that the `get_expense_by_id()` method works as expected because I can retrieve the expense by a specific id**
`{'id': 'randomId3', 'title': 'Sportwear', 'amount': 600}`

**When I tried retrieving an expense with the title of 'Healthcare', I am able to retrieve its entire object. What this means is that the `get_expense_by_title()` method also works as expected because I can retrieve the expense by a specific title**
`{'id': 'randomId1', 'title': 'Healthcare', 'amount': 100}`
