import sqlite3
from mappings import auto_classify
from datetime import datetime

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Table banayi jahan data save hoga
    # database.py mein table creation query update karo
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses 
                  (id INTEGER PRIMARY KEY, amount REAL, category TEXT, group_category TEXT, date DATE)''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
def add_expense(amount, category):
    group_cat = auto_classify(category)
    date_today = datetime.now().strftime("%Y-%m-%d")
    
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, group_category, date) VALUES (?, ?, ?, ?)", 
                   (amount, category, group_cat, date_today))
    conn.commit()
    conn.close()
    print("Expense added successfully!")
    update_balance(amount)

def get_all_expenses():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall() # Yeh list of tuples return karega
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # ID ke basis par delete karega
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print(f"Expense with ID {expense_id} deleted successfully!")

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    
    # Sahi SQL syntax: column names likhna zaroori hai!
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            balance REAL
        )
    ''')
    
    cursor.execute("INSERT OR IGNORE INTO settings (id, balance) VALUES (1, 10000.0)")
    
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM settings WHERE id = 1")
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def update_balance(amount):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Naya balance calculate karo
    current_bal = get_balance()
    new_bal = current_bal - amount
    
    cursor.execute("UPDATE settings SET balance = ? WHERE id = 1", (new_bal,))
    conn.commit()
    conn.close()

def set_balance(new_balance):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Puraana balance overwrite karo
    cursor.execute("UPDATE settings SET balance = ? WHERE id = 1", (new_balance,))
    conn.commit()
    conn.close()
def get_category_expenses():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Har category ka sum nikalo
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return data