from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

def connect():
    return sqlite3.connect("business.db")

def add_customer():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Customers
    (CustomerName,Phone,Email)
    VALUES(?,?,?)
    """,
    (
        name_entry.get(),
        phone_entry.get(),
        email_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Customer Added Successfully"
    )

    show_customers()

def show_customers():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM Customers"
    )

    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()

root = Tk()
root.title("Customer Management")
root.geometry("900x500")

Label(root,text="Customer Name").pack()
name_entry = Entry(root,width=40)
name_entry.pack()

Label(root,text="Phone").pack()
phone_entry = Entry(root,width=40)
phone_entry.pack()

Label(root,text="Email").pack()
email_entry = Entry(root,width=40)
email_entry.pack()

Button(
    root,
    text="Add Customer",
    command=add_customer,
    bg="green",
    fg="white"
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=(1,2,3,4),
    show="headings"
)

tree.heading(1,text="ID")
tree.heading(2,text="Customer Name")
tree.heading(3,text="Phone")
tree.heading(4,text="Email")

tree.pack(fill=BOTH, expand=True)

show_customers()

root.mainloop()

from tkinter import *

def open_window():
    window = Toplevel()
    window.title("Products Management")
    window.geometry("900x500")

    Label(
        window,
        text="Products Management",
        font=("Arial", 16, "bold")
    ).pack(pady=20)