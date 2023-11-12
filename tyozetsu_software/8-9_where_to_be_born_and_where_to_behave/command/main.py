from ui import SelectionUI
from usecase import BuyPetCommand, CancelBuyingCommand, Cat, Dog, PetShop


def create_pet_selection_ui(shop):
    ui = SelectionUI()
    ui.register_command("猫をください", BuyPetCommand(shop, Cat()))
    ui.register_command("犬をください", BuyPetCommand(shop, Dog()))
    ui.register_command("やっぱりやめます", CancelBuyingCommand(shop))
    return ui


shop = PetShop()
ui = create_pet_selection_ui(shop)

print(ui.help())
# 1: 猫をください
# 2: 犬をください
# 3: やっぱりやめます

user_input = int(input())
ui.select(user_input)
# 選んだ項目のコマンドが実行される
