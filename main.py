import sqlite3
from database import view_expenses , delete_expense
def add_expense(amount, category):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, date('now'))", (amount, category))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

# Simple Menu
print("Welcome to Aura Finance Tracker!")
# main.py mein yeh logic use karo
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
choice = input("Choose an option: ")

if choice == '1':
    # ... wahi purana logic ...
    amt = 0.0
    while True:
        try:
            amt = float(input("Enter amount: "))
            break  # Agar sahi number mil gaya, toh loop se bahar aa jao
        except ValueError:
            print("Error: Invalid number! Please enter a valid number.")

        cat = input("Enter category (e.g., Food, Travel): ")
        add_expense(amt, cat)
elif choice == '2':
    print("--- Here are your expenses ---")
    view_expenses()
elif choice == '3':
    print("--- Here are your expenses ---")
    view_expenses() # Pehle list dikhao taaki user ko ID pata chale
    del_id = int(input("Enter ID of expense to delete: "))
    delete_expense(del_id)