import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",  
            database="empmansys"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def Add_Employee(cursor):
    emp_id = int(input("Enter employee id: "))
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter Employee Salary: "))
    emp_dept = input("Enter Employee Dept: ")

    query = "INSERT INTO employee (emp_id, emp_name, emp_salary, emp_dept) VALUES (%s, %s, %s, %s)"
    values = (emp_id, emp_name, emp_salary, emp_dept)
    cursor.execute(query, values)
    print("Employee Added Successfully!!")

def View_Employee(cursor):
    query = "SELECT * FROM employee"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for item in results:
                print(f"ID: {item[0]} | Name: {item[1]} | Salary: {item[2]} | Dept: {item[3]}")
        else:
            print("No employees found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def Update_Employee(cursor):
    emp_id = int(input("Enter employee id to be updated: "))
    print("Enter what needs to be updated?")
    print("1. Name\n2. Salary\n3. Dept")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        new_name = input("Enter new name: ")
        query = "UPDATE employee SET emp_name = %s WHERE emp_id = %s"
        values = (new_name, emp_id)
        cursor.execute(query, values)

    elif ch == 2:
        new_salary = float(input("Enter new Salary: "))
        query = "UPDATE employee SET emp_salary = %s WHERE emp_id = %s"
        values = (new_salary, emp_id)
        cursor.execute(query, values)

    elif ch == 3:
        new_dept = input("Enter new Dept: ")
        query = "UPDATE employee SET emp_dept = %s WHERE emp_id = %s"
        values = (new_dept, emp_id)
        cursor.execute(query, values)

    print("Employee updated successfully!")

def Delete_Employee(cursor):
    emp_id = int(input("Enter employee id to delete: "))
    query = "DELETE FROM employee WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    print("Employee deleted successfully!")

def Search_Employee(cursor):
    search_term = input("Enter employee name or department to search: ")
    query = "SELECT * FROM employee WHERE emp_name LIKE %s OR emp_dept LIKE %s"
    cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()
    
    if results:
        for item in results:
            print(f"ID: {item[0]} | Name: {item[1]} | Salary: {item[2]} | Dept: {item[3]}")
    else:
        print("No employee found matching your search.")

def main():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to database. Exiting...")
        return
    cursor = connection.cursor()

    while True:
        print("\n---Employee Management Application---")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            Add_Employee(cursor)
        elif choice == 2:
            Update_Employee(cursor)
        elif choice == 3:
            Delete_Employee(cursor)
        elif choice == 4:
            View_Employee(cursor)
        elif choice == 5:
            Search_Employee(cursor)
        elif choice == 6:
            connection.commit()  
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
