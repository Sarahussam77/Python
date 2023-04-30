from manager import Manager
from employee import Employee


while True:
    user_input = input(" Enter your choose from the list:\n"
                       "1-'add' to add a new employee\n"
                       "2-'transfer' to transfer an employee\n"
                       "3-'fire' to remove an employee\n"
                       "4-'list' to listthe employees\n"
                       "5-'m' to log in as a manager\n"
                       "6-'e' to log in as an employee\n"
                       "7-'q' to quit: ")
    if user_input == "add":
        employee_type = input(
            "Enter 'm' to add a new manager or 'e' to add a new employee: ")
        first_name = input("Enter the employee's first name: ")
        last_name = input("Enter the employee's last name: ")
        age = int(input("Enter the employee's age: "))
        department = input("Enter the employee's department: ")
        salary = int(input("Enter the employee's salary: "))
        if employee_type == "m":
            managed_department = input("Enter the managed department: ")
            manager = Manager(first_name, last_name, age,
                              department, salary, managed_department)
        elif employee_type == "e":
            employee = Employee(first_name, last_name, age, department, salary)
        else:
            print("Invalid input.")

    elif user_input == "transfer":
        first_name = input("Enter the employee's first name: ")
        last_name = input("Enter the employee's last name: ")
        new_department = input("Enter the new department: ")
        employee = next((e for e in Employee.employees if e.first_name ==
                        first_name and e.last_name == last_name), None)
        if employee:
            employee.transfer(new_department)
        
        else:
            print("Employee not found.")

    elif user_input == "fire":
        first_name = input("Enter the employee's first name: ")
        last_name = input("Enter the employee's last name: ")
        Employee.fire(first_name,last_name)

    elif user_input == "list":
        Employee.list_employees()

    elif user_input == "m":
        user_input = input(
                    "Enter 'list' to list the employees or 'q' to log out: ")
        if user_input == "list":
                    Manager.list_employees()
        elif user_input == "q":
                    break
        else:
                    print("Invalid input.")
        

    elif user_input == "e":

        Employee.show()


    elif user_input == "q":
        break

    else:
        print("Invalid input.")
