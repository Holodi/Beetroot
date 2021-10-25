# School

class Person:

    def __init__(self, first_name, last_name, birthday, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def add_teacher(self):
        pass

    def add_students(self):
        pass

class Student(Person):
    pass

class Teacher(Person):

    def __init__(self, salary):
        super().__init__()
        self.salary = salary

    def add_salary(self):
        pass
