import sqlite3
from database import view_expenses
def add_expense(amount, category):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, date('now'))", (amount, category))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

# Simple Menu
print("Welcome to Aura Finance Tracker!")
amt = float(input("Enter amount: "))
cat = input("Enter category (e.g., Food, Travel): ")

add_expense(amt, cat)
print("--- Here are your expenses ---")
view_expenses()