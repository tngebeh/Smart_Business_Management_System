from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ----------------
def connect():
    return sqlite3.connect("business.db")


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Products(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT,
        Category TEXT,
        Quantity INTEGER,
        Price REAL
    )
    """)

    conn.commit()
    conn.close()


# ---------------- FUNCTIONS ----------------
def add_product():
    if not name_entry.get() or not category_entry.get():
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO Products(ProductName, Category, Quantity, Price)
    VALUES(?,?,?,?)
    """, (
        name_entry.get(),
        category_entry.get(),
        quantity_entry.get(),
        price_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Product Added")

    clear_entries()
    show_products()


def clear_entries():
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)


def show_products():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", END, values=row)


def search_category():
    category = category_search.get()

    if category == "":
        messagebox.showwarning("Warning", "Select a category")
        return

    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Products WHERE Category=?", (category,))
    rows = cur.fetchall()

    conn.close()

    for row in rows:
        tree.insert("", END, values=row)


# ---------------- UI ----------------
root = Tk()
root.title("Products Management System")
root.geometry("900x550")

create_table()

# Product Name
Label(root, text="Product Name").pack()
name_entry = Entry(root, width=40)
name_entry.pack()

# Category (Combobox - FIXED)
Label(root, text="Category").pack()
category_entry = ttk.Combobox(
    root,
    width=37,
    state="readonly",
    values=[
        "Food & Beverages",
        "Electronics",
        "Clothing",
        "Cosmetics",
        "Pharmaceuticals",
        "Stationery",
        "Household Items",
        "Furniture",
        "Construction Materials",
        "Agricultural Products",
        "Sports Equipment",
        "Services"
    ]
)
category_entry.pack()

# Quantity
Label(root, text="Quantity").pack()
quantity_entry = Entry(root, width=40)
quantity_entry.pack()

# Price
Label(root, text="Price").pack()
price_entry = Entry(root, width=40)
price_entry.pack()

# Add Button
Button(
    root,
    text="Add Product",
    command=add_product,
    bg="green",
    fg="white"
).pack(pady=10)

# Search Category
Label(root, text="Search By Category").pack()

category_search = ttk.Combobox(
    root,
    width=37,
    state="readonly",
    values=[
        "Food & Beverages",
        "Electronics",
        "Clothing",
        "Cosmetics",
        "Pharmaceuticals",
        "Stationery",
        "Household Items",
        "Furniture",
        "Construction Materials",
        "Agricultural Products",
        "Sports Equipment",
        "Services"
    ]
)
category_search.pack()

Button(
    root,
    text="Search Category",
    command=search_category,
    bg="blue",
    fg="white"
).pack(pady=5)

Button(
    root,
    text="Show All",
    command=show_products,
    bg="gray",
    fg="white"
).pack(pady=5)

# Table
tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5), show="headings")

tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="Category")
tree.heading(4, text="Quantity")
tree.heading(5, text="Price")

tree.pack(fill=BOTH, expand=True)

show_products()

root.mainloop()