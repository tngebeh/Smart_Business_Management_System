from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

def connect():
    return sqlite3.connect("business.db")

def record_payment():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Payments
    (OrderID, PaymentMethod, Amount, PaymentStatus)
    VALUES (?, ?, ?, ?)
    """,
    (
        order_entry.get(),
        method_combo.get(),
        amount_entry.get(),
        status_combo.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Payment Recorded Successfully"
    )

    show_payments()

    # =========================
    # CLEAR INPUT FIELDS
    # =========================
    order_entry.delete(0, END)
    amount_entry.delete(0, END)

    method_combo.set("")
    status_combo.set("")


def show_payments():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Payments")
    rows = cur.fetchall()

    conn.close()

    for row in rows:
        tree.insert("", END, values=row)


root = Tk()
root.title("Payment Management")
root.geometry("1000x600")

Label(root, text="Order ID").pack()
order_entry = Entry(root, width=40)
order_entry.pack()

Label(root, text="Payment Method").pack()
method_combo = ttk.Combobox(
    root,
    values=["Cash", "Mobile Money", "Bank Transfer"]
)
method_combo.pack()

Label(root, text="Amount").pack()
amount_entry = Entry(root, width=40)
amount_entry.pack()

Label(root, text="Payment Status").pack()
status_combo = ttk.Combobox(
    root,
    values=["Paid", "Unpaid"]
)
status_combo.pack()

Button(
    root,
    text="Record Payment",
    command=record_payment,
    bg="green",
    fg="white"
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=(1, 2, 3, 4, 5, 6),
    show="headings"
)

tree.heading(1, text="Payment ID")
tree.heading(2, text="Order ID")
tree.heading(3, text="Method")
tree.heading(4, text="Amount")
tree.heading(5, text="Status")
tree.heading(6, text="Date")

tree.pack(fill=BOTH, expand=True)

show_payments()

root.mainloop()