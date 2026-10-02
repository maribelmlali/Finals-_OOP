class Car:
    def move(self):
        return "The car is driving!"

class Person:
    def move(self):
        return "The person is walking!"

class Robot:
    def move(self):
        return "The robot is moving!"

def make_it_move(thing):
    print(thing.move())

for m in {Car(), Person(), Robot()}:
    make_it_move(m)   




