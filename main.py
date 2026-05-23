import sqlite3
from database import init_db, update_balance, get_all_expenses , delete_expense , get_balance ,add_expense
init_db()

# Simple Menu
print("Welcome to Aura Finance Tracker!")
# main.py mein yeh logic use karo
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Get Balance")
choice = input("Choose an option: ")

if choice == '1':
    # ... wahi purana logic ...
    amt = 0.0
    while True:
        try:
            amt = float(input("Enter amount: "))
            if amt > get_balance():
              print("ALERT: You don't have enough balance!")
            else:
              cat = input("Enter category: ")
              add_expense(amt, cat)
              update_balance(amt)
              #print("Expense added successfully.")
            break  # Agar sahi number mil gaya, toh loop se bahar aa jao
        except ValueError:
            print("Error: Invalid number! Please enter a valid number.")
elif choice == '2':
    print("--- Here are your expenses ---")
    view_expenses()
elif choice == '3':
    print("--- Here are your expenses ---")
    view_expenses() # Pehle list dikhao taaki user ko ID pata chale
    del_id = int(input("Enter ID of expense to delete: "))
    delete_expense(del_id)
# ... purana code ...
elif choice == '4':
    current_balance = get_balance()
    print(f"\n--- Current Balance: ₹{current_balance:.2f} ---\n")
# ... purana code ...