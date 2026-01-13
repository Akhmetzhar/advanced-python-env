class Employee:
    def __init__(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
    def get_role(self):
        return "Employee"

class Manager(Employee):
    def get_role(self):
        return "Manager"
    def get_bonus(self):
        return self._salary*0.1

def show(employees):
    for e in employees:
        print(e.get_role(),e.get_salary())

e1=Employee(1000)
e2=Manager(2000)

show([e1,e2])
