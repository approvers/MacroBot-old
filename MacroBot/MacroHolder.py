from MacroBot.Macro import Macro
from MacroBot.Message import Message


class MacroHolder:
    def __init__(self, data):
        self.macros = data
        print(data)
        for key, value in data.items():
            self.macros[key] = Macro(value)
        print(self.macros)

    def has_macro(self, name:str) -> bool:
        return name in self.macros

    def get_macro(self, name:str) -> Macro:
        return self.macros[name]

    def add_macro(self, name:str):
        self.macros[name] = Macro()
    def del_macro(self, name:str):
        del self.macros[name]

    async def loop(self):
        for macro in self.macros.values():
            await macro.loop()
    async def message(self, message:Message):
        for macro in self.macros.values():
            await macro.message(message)
