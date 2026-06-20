import sqlite3

# Connect to Database
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

# =========================
# USERS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE,
    Password TEXT
)
""")

# Default Admin Login
cursor.execute("""
INSERT OR IGNORE INTO Users(Username, Password)
VALUES ('admin', 'admin123')
""")

# =========================
# PRODUCTS TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL,
    Quantity INTEGER,
    Price REAL
)
""")

# =========================
# CATEGORIES TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories(
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT UNIQUE
)
""")

categories = [
    ("Food & Beverages",),
    ("Electronics",),
    ("Clothing",),
    ("Cosmetics",),
    ("Pharmaceuticals",),
    ("Stationery",),
    ("Household Items",),
    ("Furniture",),
    ("Construction Materials",),
    ("Agricultural Products",),
    ("Sports Equipment",),
    ("Services",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO Categories(CategoryName) VALUES(?)",
    categories
)

# =========================
# VENDORS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Vendors(
    VendorID INTEGER PRIMARY KEY AUTOINCREMENT,
    VendorName TEXT NOT NULL,
    Phone TEXT,
    Address TEXT
)
""")

# =========================
# CUSTOMERS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Phone TEXT,
    Email TEXT
)
""")

# =========================
# ORDERS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    TotalAmount REAL,
    OrderStatus TEXT DEFAULT 'Pending',
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =========================
# PAYMENTS TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Payments(
    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    PaymentMethod TEXT,
    Amount REAL,
    PaymentStatus TEXT,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =========================
# EXPENSES TABLE
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Expenses(
    ExpenseID INTEGER PRIMARY KEY AUTOINCREMENT,
    ExpenseName TEXT,
    Category TEXT,
    Amount REAL,
    ExpenseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")