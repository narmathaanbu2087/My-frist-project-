Expense Tracker Project (expense.py)

import json import os

FILE_NAME = "expenses.json"

Load existing expenses

def load_expenses(): if os.path.exists(FILE_NAME): with open(FILE_NAME, "r") as f: return json.load(f) return []

Save expenses

def save_expenses(expenses): with open(FILE_NAME, "w") as f: json.dump(expenses, f, indent=4)

Add expense

def add_expense(expenses): amount = float(input("Enter amount: ")) category = input("Enter category (food/travel/etc): ") note = input("Enter note: ")

expense = {
    "amount": amount,
    "category": category,
    "note": note
}

expenses.append(expense)
save_expenses(expenses)
print("Expense added successfully!\n")

View expenses

def view_expenses(expenses): if not expenses: print("No expenses found!\n") return

total = 0
print("\n--- Expense List ---")
for i, exp in enumerate(expenses, start=1):
    print(f"{i}. Amount: {exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")
    total += exp['amount']

print(f"Total Expense: {total}\n")

Main menu

def main(): expenses = load_expenses()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_expense(expenses)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")

if name == "main": main()
