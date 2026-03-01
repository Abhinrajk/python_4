
#5. Employee Salary System (Inheritance + Polymorphism)

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def calculate_salary(self):
        bonus = 0.20 * self.base_salary
        return self.base_salary + bonus


class Developer(Employee):
    def calculate_salary(self):
        bonus = 0.10 * self.base_salary
        return self.base_salary + bonus


class Intern(Employee):
    def calculate_salary(self):
        stipend = 0.05 * self.base_salary
        return self.base_salary + stipend


# Creating objects
emp1 = Manager("Rahul", 50000)
emp2 = Developer("Anjali", 40000)
emp3 = Intern("Arun", 20000)

employees = [emp1, emp2, emp3]

for emp in employees:
    print("Employee Name:", emp.name)
    print("Total Salary:", emp.calculate_salary())
    print()