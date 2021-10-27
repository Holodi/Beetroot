#Method overloading

class Animal:

    def talk(self):
        return ":-)"


class Dog(Animal):

    def talk(self):
        return "Woof! Woof!"


class Cat(Animal):

    def talk(self):
        return "Meeooow!"


def animal_say(animal):
    print(animal.talk())


animal_say(Dog())
animal_say(Cat())
