class Pet:
    def reaction(self):
        print("sum reaction")


class Customer:
    def touch(self, pet: Pet):
        pet.reaction()


class Dog(Pet):
    def reaction(self):
        print("Bow-Wow!")


class Cat(Pet):
    def reaction(self):
        print("Meow-Meow!")


customer = Customer()
customer.touch(Dog())
customer.touch(Cat())

"""
$ python polymorphism.py 
Bow-Wow!
Meow-Meow!
"""
