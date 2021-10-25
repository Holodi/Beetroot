class Dog():

    AGE_FACTOR = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * self.AGE_FACTOR

def task2(age):
    dog_age = Dog(age)
    print(f"Dog age = {dog_age.age}. In human equivalen = {dog_age.human_age()}")
