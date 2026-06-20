from tkinter import *
from tkinter import messagebox
import sqlite3

# =========================
# LOGIN FUNCTION
# =========================
def login():

    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("business.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM Users WHERE Username=? AND Password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Success", "Login Successful")

        root.destroy()

        # Open Dashboard
        import dashboard

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# =========================
# CLEAR FIELDS
# =========================
def clear():

    entry_username.delete(0, END)
    entry_password.delete(0, END)


# =========================
# EXIT SYSTEM
# =========================
def exit_system():

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# =========================
# GUI WINDOW
# =========================
root = Tk()
root.title("Smart Business Management System")
root.geometry("500x350")
root.resizable(False, False)

# =========================
# HEADING
# =========================
Label(
    root,
    text="SMART BUSINESS MANAGEMENT SYSTEM",
    font=("Arial", 14, "bold")
).pack(pady=20)

# =========================
# USERNAME
# =========================
Label(
    root,
    text="Username",
    font=("Arial", 11)
).pack()

entry_username = Entry(
    root,
    width=30,
    font=("Arial", 11)
)
entry_username.pack(pady=5)

# =========================
# PASSWORD
# =========================
Label(
    root,
    text="Password",
    font=("Arial", 11)
).pack()

entry_password = Entry(
    root,
    width=30,
    show="*",
    font=("Arial", 11)
)
entry_password.pack(pady=5)

# =========================
# BUTTONS
# =========================
Button(
    root,
    text="Login",
    width=15,
    bg="green",
    fg="white",
    command=login
).pack(pady=10)

Button(
    root,
    text="Clear",
    width=15,
    command=clear
).pack(pady=5)

Button(
    root,
    text="Exit",
    width=15,
    bg="red",
    fg="white",
    command=exit_system
).pack(pady=5)

root.mainloop()