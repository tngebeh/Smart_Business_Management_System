from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

def connect():
    return sqlite3.connect("business.db")

def add_vendor():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Vendors
    (VendorName,Phone,Address)
    VALUES(?,?,?)
    """,
    (
        name_entry.get(),
        phone_entry.get(),
        address_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Vendor Added Successfully"
    )

    show_vendors()

def show_vendors():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM Vendors"
    )

    rows = cur.fetchall()

    for row in rows:
        tree.insert("",END,values=row)

    conn.close()

root = Tk()
root.title("Vendor Management")
root.geometry("900x500")

Label(root,text="Vendor Name").pack()
name_entry = Entry(root,width=40)
name_entry.pack()

Label(root,text="Phone").pack()
phone_entry = Entry(root,width=40)
phone_entry.pack()

Label(root,text="Address").pack()
address_entry = Entry(root,width=40)
address_entry.pack()

Button(
    root,
    text="Add Vendor",
    command=add_vendor,
    bg="blue",
    fg="white"
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=(1,2,3,4),
    show="headings"
)

tree.heading(1,text="ID")
tree.heading(2,text="Vendor")
tree.heading(3,text="Phone")
tree.heading(4,text="Address")

tree.pack(fill=BOTH,expand=True)

show_vendors()

root.mainloop()