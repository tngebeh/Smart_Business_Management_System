from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

def connect():
    return sqlite3.connect("business.db")

def add_expense():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Expenses
    (ExpenseName,Category,Amount)
    VALUES(?,?,?)
    """,
    (
        expense_entry.get(),
        category_combo.get(),
        amount_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Expense Added Successfully"
    )

    show_expenses()

def show_expenses():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM Expenses"
    )

    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()

root = Tk()
root.title("Expense Tracker")
root.geometry("1000x600")

Label(root,text="Expense Name").pack()
expense_entry = Entry(root,width=40)
expense_entry.pack()

Label(root,text="Category").pack()

category_combo = ttk.Combobox(
    root,
    values=[
        "Transport",
        "Fuel",
        "Salary",
        "Rent",
        "Electricity",
        "Internet",
        "Other"
    ]
)
category_combo.pack()

Label(root,text="Amount").pack()
amount_entry = Entry(root,width=40)
amount_entry.pack()

Button(
    root,
    text="Add Expense",
    command=add_expense,
    bg="red",
    fg="white"
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=(1,2,3,4,5),
    show="headings"
)

tree.heading(1,text="Expense ID")
tree.heading(2,text="Expense")
tree.heading(3,text="Category")
tree.heading(4,text="Amount")
tree.heading(5,text="Date")

tree.pack(fill=BOTH, expand=True)

show_expenses()

root.mainloop()