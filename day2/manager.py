from employee import Employee
class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department=managed_department
    def show(self):
        super().show()
        print(f"Managed Department: {self.managed_department}")