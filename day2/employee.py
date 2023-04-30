from mysql.connector import connect, Error
# MySQL database configuration
try:
    config = {
    'user': 'root',
    'password': '',
    'port': '3307',
    'host': '127.0.0.1',
    'database': 'employee',
    'auth_plugin': 'mysql_native_password'
    }
    cnx = connect(**config)
    if cnx.is_connected():
     print("successfully connected")
except Error as e:
    print(e)


class Employee:
    employees=[]
    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees.append(self)
        self.insert()
    def insert(self):
        cursor = cnx.cursor()
        add_employee = ("INSERT INTO employee "
                        "(first_name, last_name, age, department, salary) "
                        "VALUES (%s, %s, %s, %s, %s)")
        employee_data = (self.first_name, self.last_name,
                         self.age, self.department, self.salary)
        cursor.execute(add_employee, employee_data)
        cnx.commit()
        print("Your record inserted successfully.")
    def transfer(self,new_department):
        # Change employee department
        self.department = new_department
        #change in db
        cursor = cnx.cursor()
        update_employee = ("UPDATE employee SET department = %s WHERE first_name = %s AND last_name = %s")
        employee_data = (self.department,self.first_name, self.last_name)
        cursor.execute(update_employee,employee_data)
        cnx.commit()
        print("Your employee transfered successfully.")
    def fire(fname,lname):
        # Remove the employee from the shared list
        remove_emp=next((emp for emp in Employee.employees if emp.first_name == fname and emp.last_name==lname), None)
        Employee.employees.remove(remove_emp)
        # Delete from the database
        cursor = cnx.cursor()
        delete_employee = ("DELETE FROM employee "
                           "WHERE first_name = %s AND last_name = %s")
        employee_data = (fname, lname)
        cursor.execute(delete_employee, employee_data)
        cnx.commit()
        print("Employee removed successfully.")
    def show():
        # Print all employee data
        print (*Employee.employees, sep="\n")

    @staticmethod
    def list_employees():
        # Select all employees and print their data
        cursor = cnx.cursor()
        select_employees = ("SELECT first_name, last_name, age, department, salary "
                 "FROM employee")
        cursor.execute(select_employees)
        for (first_name, last_name, age, department, salary) in cursor:
            print(f"Name: {first_name} {last_name}")
            print(f"Age: {age}")
            print(f"Department: {department}")
            print(f"Salary: {salary}")


