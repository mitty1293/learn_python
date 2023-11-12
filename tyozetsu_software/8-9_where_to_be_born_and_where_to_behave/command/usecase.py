from typing import Type

from common import CommandInterface


class PetShop:
    pass


class Pet:
    pass


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class BuyPetCommand(CommandInterface):
    def __init__(self, shop: Type[PetShop], pet: Type[Pet]):
        self.shop = shop
        self.pet = pet

    def invoke(self) -> None:
        # self.shop と self.pet を使って購入を処理する
        pass


class CancelBuyingCommand(CommandInterface):
    def __init__(self, shop: Type[PetShop]):
        self.shop = shop

    def invoke(self) -> None:
        # self.shop に対してキャンセルを申し出る
        pass
