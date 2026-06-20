Project Overview
The Smart Business Management System (SBMS) is a GUI-based desktop application developed using Python, Tkinter, and SQLite. The system is designed to help small and medium-sized businesses manage their daily operations efficiently through inventory management, customer management, vendor management, sales tracking, expense tracking, payment processing, and business reporting.
The application provides a centralized platform for monitoring business activities and generating useful reports for decision-making.

Objectives
The main objectives of this project are:
1. Manage products and inventory.
2. Categorize products into different groups.
3. Manage customer information.
4. Manage vendor information.
5.  Process customer orders.
6. Track payments.
7. Track business expenses.
8.  Generate weekly sales reports.
9. Calculate business profits.
10. Monitor stock levels.
11. Improve business decision-making.


Technologies Used
Programming Language
 Python 3

GUI Framework
- Tkinter

Database
- SQLite3

Development Environment

- Visual Studio Code (VS Code)



System Features

User Authentication

The system provides a secure login page for administrators.

Default Login

Username:
admin

Password:
admin123

Product Management
The Product Management Module allows users to:
- Add products
- Update products
- Delete products
- View products
- Categorize products
- Monitor stock quantity


Product Categories
- Food & Beverages
- Electronics
- Clothing
- Cosmetics
- Pharmaceuticals
- Stationery
- Household Items
- Furniture
- Construction Materials
- Agricultural Products
- Sports Equipment
- Services


Vendor Management
The Vendor Module allows users to:
- Add vendors
- Update vendor information
- Delete vendors
- Store vendor phone numbers
- Store vendor addresses
- Search vendors


Customer Management
The Customer Module allows users to:
- Add customers
- Update customer information
- Delete customers
- Store customer phone numbers
- Store customer emails



Order Management
The Order Module allows users to:
- Place customer orders
- Select products
- Specify quantities
- Automatically calculate totals
- Reduce stock after purchase
- Track order status

Order Status
- Pending
- Delivered

Payment Management
The Payment Module allows users to:
- Record payments
- Track payment status
- Monitor transactions

Payment Methods
- Cash
- Mobile Money
- Bank Transfer

Payment Status
- Paid
- Unpaid


Expense Management
The Expense Module allows users to:

- Record business expenses
- Categorize expenses
 Monitor spending

Expense Categories
- Transport
- Fuel
- Salary
- Rent
- Electricity
- Internet
- Other



Reporting Module

The Reporting Module provides:

Weekly Sales Report

Displays total sales for the last seven days.

Weekly Expense Report

Displays total expenses for the last seven days.

Weekly Profit Report

Profit = Sales − Expenses

Total Business Summary

Displays:

- Total Sales
- Total Expenses
- Total Profit



Inventory Monitoring

The system automatically tracks stock levels.

Low Stock Alert

A warning message is displayed whenever stock falls below five units.


Receipt Generation
The system generates a receipt file whenever an order is placed.
Receipt information includes:
- Customer Name
- Product Name
- Quantity Purchased
- Total Amount
- Order Status


Dashboard

The Dashboard provides a summary of:

- Total Products
- Total Customers
- Total Vendors
- Total Orders
- Weekly Sales
- Weekly Expenses
- Total Profit
- Delivered Orders
- Pending Orders

It also displays product statistics by category.


Database Structure

Users

- UserID
- Username
- Password

Products

- ProductID
- ProductName
- Category
- Quantity
- Price

Categories

- CategoryID
- CategoryName

Vendors

- VendorID
- VendorName
- Phone
- Address

Customers

- CustomerID
- CustomerName
- Phone
- Email

Orders
- OrderID
- CustomerID
- ProductID
- Quantity
- TotalAmount
- OrderStatus
- OrderDate

Payments
- PaymentID
- OrderID
- PaymentMethod
- Amount
- PaymentStatus
- PaymentDate

Expenses
- ExpenseID
- ExpenseName
- Category
- Amount
- ExpenseDate


System Workflow
1. User launches the application.
2. Login page appears.
3. User enters credentials.
4. Dashboard opens.
5. User manages products, vendors, customers, and orders.
6. Payments and expenses are recorded.
7. Reports are generated automatically.
8. Profit is calculated from sales and expenses.


SDG Alignment

This project supports:

SDG 8 – Decent Work and Economic Growth

The system promotes business efficiency through:

- Financial monitoring
- Inventory management
- Sales tracking
- Expense tracking
- Vendor management
- Customer management
- Profit analysis

This helps small businesses improve productivity and make informed business decisions.


Future Improvements

Future versions may include:
- Barcode Scanner Integration
- QR Code Payments
- Email Notifications
- SMS Notifications
- Multi-User Access Control
- Cloud Database Integration
- Business Analytics Charts
- Mobile Application Support

---

Author

Smart Business Management System (SBMS)

Developed as a GUI-Based Python Application Project using Python, Tkinter, and SQLite.

© 2026 All Rights Reserved.
