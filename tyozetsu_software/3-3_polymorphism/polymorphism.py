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
どんなPetであろうとtouchすればreactionが起きる
Petオブジェクト毎に異なる機能や動作を示すことができる
PetとCustomerはこの二者だけで完結しており, 具体的なDogやCatには興味を持たない

実行される処理の実体がコールされたメソッドではなく, メソッドを持つオブジェクトによって決定される性質.
またこの性質を使って, 同一のメソッドを使って, オブジェクトごとに異なった処理を行わせること.
-> 多態性

$ python polymorphism.py 
Bow-Wow!
Meow-Meow!
"""
