from tkinter import *
import sqlite3

def connect():
    return sqlite3.connect("business.db")

def get_weekly_sales():
    try:
        conn = connect()
        cur = conn.cursor()
        # Using '-' instead of ' ' in modifiers can sometimes cause issues; 
        # '-7 days' is standard in SQLite
        cur.execute("""
        SELECT IFNULL(SUM(TotalAmount), 0)
        FROM Orders
        WHERE OrderDate >= date('now', '-7 days')
        """)
        result = cur.fetchone()[0]
        conn.close()
        return result
    except sqlite3.OperationalError:
        return 0  # Fallback if table doesn't exist yet

def get_weekly_expenses():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT IFNULL(SUM(Amount), 0)
        FROM Expenses
        WHERE ExpenseDate >= date('now', '-7 days')
        """)
        result = cur.fetchone()[0]
        conn.close()
        return result
    except sqlite3.OperationalError:
        return 0

def get_total_sales():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT IFNULL(SUM(TotalAmount), 0)
        FROM Orders
        """)
        result = cur.fetchone()[0]
        conn.close()
        return result
    except sqlite3.OperationalError:
        return 0

def get_total_expenses():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT IFNULL(SUM(Amount), 0)
        FROM Expenses
        """)
        result = cur.fetchone()[0]
        conn.close()
        return result
    except sqlite3.OperationalError:
        return 0

# --- Fetch Data ---
weekly_sales = get_weekly_sales()
weekly_expenses = get_weekly_expenses()
total_sales = get_total_sales()
total_expenses = get_total_expenses()

# Calculate profit
profit = weekly_sales - weekly_expenses

# --- UI Setup ---
root = Tk()
root.title("Business Reports")
root.geometry("700x500")

Label(
    root,
    text="BUSINESS REPORTS",
    font=("Arial", 18, "bold")
).pack(pady=20)

Label(
    root,
    text=f"Weekly Sales: Le {weekly_sales:,}", # Added comma formatting for clean currency views
    font=("Arial", 14)
).pack(pady=10)

Label(
    root,
    text=f"Weekly Expenses: Le {weekly_expenses:,}",
    font=("Arial", 14)
).pack(pady=10)

# Dynamic color for profit/loss
profit_color = "green" if profit >= 0 else "red"
profit_label_text = f"Weekly Profit: Le {profit:,}" if profit >= 0 else f"Weekly Loss: Le {abs(profit):,}"

Label(
    root,
    text=profit_label_text,
    font=("Arial", 14, "bold"),
    fg=profit_color
).pack(pady=10)

Label(
    root,
    text=f"Total Sales: Le {total_sales:,}",
    font=("Arial", 14)
).pack(pady=10)

Label(
    root,
    text=f"Total Expenses: Le {total_expenses:,}",
    font=("Arial", 14)
).pack(pady=10)

root.mainloop()