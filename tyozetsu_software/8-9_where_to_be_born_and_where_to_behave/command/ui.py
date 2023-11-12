from typing import List

from common import CommandInterface


class SelectionItem:
    def __init__(self, label: str, command: CommandInterface):
        self.label = label
        self.command = command


class SelectionUI:
    def __init__(self):
        self.selection_items: List[SelectionItem] = []

    def register_command(self, label: str, command: CommandInterface) -> None:
        self.selection_items.append(SelectionItem(label, command))

    def help(self) -> str:
        indexed_item_list = [
            f"{i + 1}: {item.label}" for i, item in enumerate(self.selection_items)
        ]
        return "\n".join(indexed_item_list)

    def select(self, number: int) -> None:
        command = self.selection_items[number - 1].command
        command.invoke()
