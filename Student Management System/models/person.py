class Person():
    """A abstract base class for every person in school family."""
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
    
    def get_id(self):
        """Get id from database and set to instance attribute"""
        pass

class Student(Person):
    """A Model of students that controls student data and some operations."""

    def __init__(self, name, age, address, phone, grade):
        super().__init__(name, age, address, phone)
        self.grade = grade
    

class Teacher(Person):
    """A Model of students that controls student data and some operations."""
    def __init__(self, name, age, address, phone, subject, salary):
        super().__init__(name, age, address, phone)
        self.subject = subject
        self.salary = salary