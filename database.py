import sqlite3

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # Table banayi jahan data save hoga
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()

def view_expenses():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    # ID ke basis par delete karega
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print(f"Expense with ID {expense_id} deleted successfully!")