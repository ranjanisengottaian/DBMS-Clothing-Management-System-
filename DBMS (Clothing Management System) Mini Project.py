#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install mysql-connector-python


# In[12]:


import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='cloth',
            user='root',    # Replace with your MySQL username
            password='Ranjani@1904' # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


# In[3]:


import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a connection to MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',    # Replace with your MySQL username
            password='Ranjani@1904', # Replace with your MySQL password
            database='cloth'  # Update to 'cloth'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def initialize_db():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS cloth")
            
            # Use the database
            cursor.execute("USE cloth")

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Items (
                ItemID INT AUTO_INCREMENT PRIMARY KEY,
                ItemName VARCHAR(255) NOT NULL,
                Price DECIMAL(10, 2) NOT NULL
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Purchases (
                PurchaseID INT AUTO_INCREMENT PRIMARY KEY,
                ItemID INT,
                Quantity INT,
                FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
            )
            ''')

            connection.commit()
            print("Tables created successfully")
        except Error as e:
            print("Error while creating tables", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def add_item(item_name, price):
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("USE cloth")  # Ensure to use the 'cloth' database
            cursor.execute('''
            INSERT INTO Items (ItemName, Price) VALUES (%s, %s)
            ''', (item_name, price))
            connection.commit()
            print(f"Item '{item_name}' with price {price} added successfully")
        except Error as e:
            print("Error while adding item", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def add_purchase(item_name, quantity):
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("USE cloth")  # Ensure to use the 'cloth' database
            
            # Get the ItemID for the given item_name
            cursor.execute('''
            SELECT ItemID FROM Items WHERE ItemName = %s
            ''', (item_name,))
            item_id = cursor.fetchone()
            
            if item_id is None:
                print(f"Item '{item_name}' does not exist.")
                return
            
            item_id = item_id[0]
            
            cursor.execute('''
            INSERT INTO Purchases (ItemID, Quantity) VALUES (%s, %s)
            ''', (item_id, quantity))
            connection.commit()
            print(f"Purchase of {quantity} '{item_name}' added successfully")
        except Error as e:
            print("Error while adding purchase", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def display_total_cost():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("USE cloth")  # Ensure to use the 'cloth' database
            cursor.execute('''
            SELECT Items.ItemName, Items.Price, Purchases.Quantity, (Items.Price * Purchases.Quantity) as TotalCost
            FROM Purchases
            JOIN Items ON Purchases.ItemID = Items.ItemID
            ''')
            purchases = cursor.fetchall()
            print(f"{'Item Name':<20} {'Price':<10} {'Quantity':<10} {'Total Cost':<10}")
            for purchase in purchases:
                print(f"{purchase[0]:<20} {purchase[1]:<10} {purchase[2]:<10} {purchase[3]:<10}")
        except Error as e:
            print("Error while fetching purchases", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def display_total_purchased_cost():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("USE cloth")  # Ensure to use the 'cloth' database
            cursor.execute('''
            SELECT SUM(Items.Price * Purchases.Quantity) as TotalPurchasedCost
            FROM Purchases
            JOIN Items ON Purchases.ItemID = Items.ItemID
            ''')
            total_cost = cursor.fetchone()[0]
            print(f"Total cost of all items purchased: {total_cost}")
        except Error as e:
            print("Error while fetching total purchased cost", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def view_items():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("USE cloth")  # Ensure to use the 'cloth' database
            cursor.execute('''
            SELECT * FROM Items
            ''')
            items = cursor.fetchall()
            print(f"{'Item ID':<10} {'Item Name':<20} {'Price':<10}")
            for item in items:
                print(f"{item[0]:<10} {item[1]:<20} {item[2]:<10}")
        except Error as e:
            print("Error while fetching items", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Main function to get input from the user
def main():
    # Initialize the database
    initialize_db()

    while True:
        print("\n1. Add Item")
        print("2. Add Purchase")
        print("3. Display Total Cost")
        print("4. View Items")
        print("5. Display Total Purchased Cost")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            price = float(input("Enter price: "))
            add_item(item_name, price)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_purchase(item_name, quantity)
        elif choice == '3':
            display_total_cost()
        elif choice == '4':
            view_items()
        elif choice == '5':
            display_total_purchased_cost()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[2]:


import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a connection to MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',    # Replace with your MySQL username
            password='Ranjani@1904', # Replace with your MySQL password
            database='clothingmanagement'  # Replace with your database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def create_table():
    """Create the Employees table in the database."""
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Employees (
                    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
                    FirstName VARCHAR(255) NOT NULL,
                    LastName VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) UNIQUE,
                    Age INT
                )
            ''')
            print("Table created successfully")
        except Error as e:
            print("Error while creating table", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def add_employee():
    """Add an employee to the Employees table."""
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            first_name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            email = input("Enter employee's email: ")
            age = int(input("Enter employee's age: "))
            cursor.execute('''
                INSERT INTO Employees (FirstName, LastName, Email, Age)
                VALUES (%s, %s, %s, %s)
            ''', (first_name, last_name, email, age))
            connection.commit()
            print("Employee added successfully")
        except Error as e:
            print("Error while adding employee", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def view_employee_details():
    """View details of all employees."""
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM Employees
            ''')
            employees = cursor.fetchall()
            if employees:
                print("EmployeeID\tFirstName\tLastName\tEmail\tAge")
                for employee in employees:
                    print("\t".join(map(str, employee)))  # Print all columns as a tab-separated string
            else:
                print("No employees found.")
        except Error as e:
            print("Error while fetching employee details", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Initialize the database and create the Employees table
create_table()

while True:
    print("\n1. Add Employee")
    print("2. View Employee Details")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employee_details()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:





# In[ ]:




