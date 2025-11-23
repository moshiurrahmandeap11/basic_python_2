# Inheritance Class Task

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def details(self):
        return f"Name: {self.name}, age: {self.age}, roll: {self.roll}"
    

# example usage
student = Student("Moshiur", 24, 1)
print(student.details())