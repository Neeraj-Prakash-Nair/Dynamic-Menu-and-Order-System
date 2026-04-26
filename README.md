# Dynamic-Menu-and-Order-System
A menu-driven restaurant management system built using Python and MySQL, supporting role-based login for cashiers and admins. Includes features such as dynamic menu handling, order processing, and automated billing with CGST/SGST calculation.



**Features**


**User (Cashier)**
  Login authentication
  Browse food categories and items
  Place orders through a menu-driven interface
  Automatic bill generation
  Tax calculation (CGST & SGST)

  
**Administrator**
  Secure login system
  Add new menu items
  Modify existing items
  Delete items
  View complete menu database


**Tech Stack**
  Language: Python
  Database: MySQL
  Libraries:
  mysql.connector (database connectivity)
  prettytable (tabular display)
  colorama (colored CLI output)
  pickle (authentication storage)
  
**Project Structure**
├── Cashierfunction.py
├── Adminfunction.py
├── Authentication.py
├── Credentials.py
├── usercredentials.dat
├── admincredentials.dat


**Setup Instructions**
  Install required libraries:
  pip install mysql-connector-python prettytable colorama
  Run the authentication file:
  python Authentication.py

  
**Key Concepts Used**
  Menu-driven programming
  File handling (binary files with pickle)
  Database operations (CRUD)
  Role-based access control
  Exception handling
  CLI design

Developed as part of CBSE Class 12 Computer Science curriculum.
