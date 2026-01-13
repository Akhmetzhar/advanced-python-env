class Person:
    def __init__(self,name):
        self._name=name
    def get_role(self):
        return "Person"

class Student(Person):
    def get_role(self):
        return "Student"

p=Person("Alex")
s=Student("Bob")

print(p.get_role())
print(s.get_role())
