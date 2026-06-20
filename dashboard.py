from tkinter import *
import sqlite3
from importlib import reload  # Required to allow opening windows multiple times


# =========================
# DATABASE COUNTS
# =========================
def get_count(table):
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    conn.close()
    return count


# =========================
# CATEGORY COUNTS
# =========================
def category_count(category):
    conn = sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM Products WHERE Category=?",
        (category,)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count


# =========================
# TOTAL SALES
# =========================
def total_sales():
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT IFNULL(SUM(TotalAmount),0) FROM Orders"
    )
    total = cursor.fetchone()[0]
    conn.close()
    return total


# =========================
# TOTAL EXPENSES
# =========================
def total_expenses():
    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT IFNULL(SUM(Amount),0) FROM Expenses"
    )
    total = cursor.fetchone()[0]
    conn.close()
    return total


# =========================
# PROFIT
# =========================
def profit():
    return total_sales() - total_expenses()


# =========================
# OPEN MODULES (FIXED FOR MULTIPLE CLICKS)
# =========================
def open_products():
    import products
    reload(products)
    try:
        products.open_window()
    except AttributeError:
        pass  # Safe fallback if window code runs on raw import


def open_vendors():
    import vendors
    reload(vendors)
    try:
        vendors.open_window()
    except AttributeError:
        pass


def open_customers():
    import customers
    reload(customers)
    try:
        customers.open_window()
    except AttributeError:
        pass


def open_orders():
    import orders
    reload(orders)
    try:
        orders.open_window()
    except AttributeError:
        pass


def open_payments():
    import payments
    reload(payments)
    try:
        payments.open_window()
    except AttributeError:
        pass


def open_expenses():
    import expenses
    reload(expenses)
    try:
        expenses.open_window()
    except AttributeError:
        pass


def open_reports():
    import reports
    reload(reports)
    try:
        reports.open_window()
    except AttributeError:
        pass


# =========================
# DASHBOARD WINDOW
# =========================
root = Tk()
root.title("Smart Business Management System")
root.geometry("900x650")

title = Label(
    root,
    text="SMART BUSINESS MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)


# =========================
# STATISTICS FRAME
# =========================
frame = Frame(root)
frame.pack(pady=10)

Label(
    frame,
    text=f"Products: {get_count('Products')}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=0, column=0, padx=10, pady=10)

Label(
    frame,
    text=f"Vendors: {get_count('Vendors')}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=0, column=1, padx=10)

Label(
    frame,
    text=f"Customers: {get_count('Customers')}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=0, column=2, padx=10)

Label(
    frame,
    text=f"Orders: {get_count('Orders')}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=1, column=0, padx=10)

Label(
    frame,
    text=f"Sales: Le {total_sales()}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=1, column=1, padx=10)

Label(
    frame,
    text=f"Expenses: Le {total_expenses()}",
    font=("Arial", 12, "bold"),
    width=20
).grid(row=1, column=2, padx=10)

Label(
    frame,
    text=f"Profit: Le {profit()}",
    font=("Arial", 12, "bold"),
    fg="green",
    width=20
).grid(row=2, column=1, pady=10)


# =========================
# PRODUCT CATEGORIES
# =========================
Label(
    frame,
    text=f"Food: {category_count('Food & Beverages')}",
    font=("Arial", 11, "bold")
).grid(row=3, column=0, pady=10)

Label(
    frame,
    text=f"Electronics: {category_count('Electronics')}",
    font=("Arial", 11, "bold")
).grid(row=3, column=1)

Label(
    frame,
    text=f"Clothing: {category_count('Clothing')}",
    font=("Arial", 11, "bold")
).grid(row=3, column=2)

Label(
    frame,
    text=f"Services: {category_count('Services')}",
    font=("Arial", 11, "bold")
).grid(row=4, column=1)


# =========================
# MODULE BUTTONS
# =========================
buttons = Frame(root)
buttons.pack(pady=20)

Button(
    buttons,
    text="Products",
    width=20,
    command=open_products
).grid(row=0, column=0, padx=10, pady=10)

Button(
    buttons,
    text="Vendors",
    width=20,
    command=open_vendors
).grid(row=0, column=1, padx=10, pady=10)

Button(
    buttons,
    text="Customers",
    width=20,
    command=open_customers
).grid(row=0, column=2, padx=10, pady=10)

Button(
    buttons,
    text="Orders",
    width=20,
    command=open_orders
).grid(row=1, column=0, padx=10, pady=10)

Button(
    buttons,
    text="Payments",
    width=20,
    command=open_payments
).grid(row=1, column=1, padx=10, pady=10)

Button(
    buttons,
    text="Expenses",
    width=20,
    command=open_expenses
).grid(row=1, column=2, padx=10, pady=10)

Button(
    buttons,
    text="Reports",
    width=20,
    command=open_reports
).grid(row=2, column=1, pady=10)

def on_closing():
    root.destroy()
    exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()