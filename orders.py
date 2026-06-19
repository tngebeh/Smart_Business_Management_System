from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
import sqlite3
from datetime import datetime


def connect():
    return sqlite3.connect("business.db")


# =========================
# RECEIPT GENERATOR (UPDATED)
# =========================

def generate_receipt(customer, product, quantity, total):
    filename = f"receipt_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    
    receipt_text = f"""==================================
SMART BUSINESS MANAGEMENT SYSTEM

Customer : {customer}
Product  : {product}
Quantity : {quantity}
Total    : Le {total}

Status   : Pending

Thank You For Your Purchase
==================================
"""
    # 1. Save to .txt file as usual
    with open(filename, "w") as file:
        file.write(receipt_text)
        
    # 2. Clear old text and post it directly onto the interface
    receipt_display.config(state=NORMAL)  # Temporarily unlock to edit
    receipt_display.delete('1.0', END)
    receipt_display.insert(END, receipt_text)
    receipt_display.config(state=DISABLED) # Relock it so users can't manually edit it


# =========================
# PLACE ORDER
# =========================

def place_order():
    try:
        product_id = product_entry.get()
        customer_id = customer_entry.get()
        quantity_str = quantity_entry.get()

        if not product_id or not customer_id or not quantity_str:
            messagebox.showerror("Error", "All entry fields must be filled")
            return

        quantity = int(quantity_str)

        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT ProductName, Price, Quantity FROM Products WHERE ProductID=?",
            (product_id,)
        )
        product = cur.fetchone()

        if not product:
            messagebox.showerror("Error", "Product Not Found")
            conn.close()
            return

        product_name = product[0]
        price = product[1]
        stock = product[2]

        if quantity > stock:
            messagebox.showerror("Error", "Insufficient Stock")
            conn.close()
            return

        total = quantity * price

        cur.execute(
            "SELECT CustomerName FROM Customers WHERE CustomerID=?",
            (customer_id,)
        )
        customer = cur.fetchone()

        if not customer:
            messagebox.showerror("Error", "Customer Not Found")
            conn.close()
            return

        customer_name = customer[0]

        cur.execute("""
        INSERT INTO Orders
        (CustomerID, ProductID, Quantity, TotalAmount, OrderStatus)
        VALUES(?,?,?,?,?)
        """, (customer_id, product_id, quantity, total, "Pending"))

        new_stock = stock - quantity
        cur.execute("""
        UPDATE Products
        SET Quantity=?
        WHERE ProductID=?
        """, (new_stock, product_id))

        if new_stock < 5:
            messagebox.showwarning(
                "Low Stock Alert",
                f"{product_name} is running low."
            )

        conn.commit()
        conn.close()

        generate_receipt(customer_name, product_name, quantity, total)

        messagebox.showinfo("Success", "Order Placed Successfully")
        
        # Clear fields for the next entry
        customer_entry.delete(0, END)
        product_entry.delete(0, END)
        quantity_entry.delete(0, END)
        
        show_orders()

    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number")


# =========================
# MARK DELIVERED
# =========================

def mark_delivered():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select an order first")
        return

    values = tree.item(selected, "values")
    order_id = values[0]

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    UPDATE Orders
    SET OrderStatus='Delivered'
    WHERE OrderID=?
    """, (order_id,))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Order Marked As Delivered")
    show_orders()


# =========================
# SHOW ORDERS
# =========================

def show_orders():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Orders")
    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    conn.close()


# =========================
# GUI SETUP
# =========================

root = Tk()
root.title("Orders Management")
root.geometry("1100x650")

# --- Top Section: Controls Layout ---
top_frame = Frame(root)
top_frame.pack(fill=X, padx=15, pady=10)

# Left Layout Frame (Inputs and Buttons)
left_frame = Frame(top_frame)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)

Label(left_frame, text="Customer ID", font=("Arial", 10, "bold")).pack(anchor=W, pady=(5, 2))
customer_entry = Entry(left_frame, width=45)
customer_entry.pack(anchor=W, pady=2)

Label(left_frame, text="Product ID", font=("Arial", 10, "bold")).pack(anchor=W, pady=(5, 2))
product_entry = Entry(left_frame, width=45)
product_entry.pack(anchor=W, pady=2)

Label(left_frame, text="Quantity", font=("Arial", 10, "bold")).pack(anchor=W, pady=(5, 2))
quantity_entry = Entry(left_frame, width=45)
quantity_entry.pack(anchor=W, pady=2)

btn_frame = Frame(left_frame)
btn_frame.pack(anchor=W, pady=15)

Button(btn_frame, text="Place Order", command=place_order, bg="green", fg="white", width=15, font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)
Button(btn_frame, text="Mark Delivered", command=mark_delivered, bg="blue", fg="white", width=15, font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)

# Right Layout Frame (Live Receipt Window View)
right_frame = LabelFrame(top_frame, text=" Live Receipt View ", font=("Arial", 10, "bold"), padx=10, pady=5)
right_frame.pack(side=RIGHT, fill=BOTH, expand=False)

receipt_display = scrolledtext.ScrolledText(right_frame, width=45, height=12, font=("Courier", 10))
receipt_display.insert(END, "\n\n   [ No active order processed yet ]")
receipt_display.config(state=DISABLED)  # Starts locked down 
receipt_display.pack()

# --- Bottom Section: Order Table ---
table_frame = Frame(root)
table_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

tree = ttk.Treeview(table_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings")

tree.heading(1, text="Order ID")
tree.heading(2, text="Customer ID")
tree.heading(3, text="Product ID")
tree.heading(4, text="Quantity")
tree.heading(5, text="Total Amount")
tree.heading(6, text="Order Status")
tree.heading(7, text="Order Date")

tree.pack(fill=BOTH, expand=True)

show_orders()
root.mainloop()