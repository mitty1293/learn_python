class Customer:
    def touch(self, pet):
        pet.reaction()


class Dog:
    def reaction(self):
        print("Bow-Wow!")


class Cat:
    def reaction(self):
        print("Meow-Meow!")


customer = Customer()
customer.touch(Dog())
customer.touch(Cat())

"""
ダックタイピング
明示的な分類であるPetクラスがなくても同じ名前のreactionメソッドを使用することができる.
共通のメソッドを持ちさえすれば継承を使わなくても, どのようなオブジェクトでもreactionメソッドを実行できる.
「型」より「ふるまい」に注目したスタイルである.

$ python polymorphism_duck_typing.py
Bow-Wow!
Meow-Meow!
"""
