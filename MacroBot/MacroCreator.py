from MacroBot.ModeHolder import ModeHolder
from MacroBot.MacroHolder import MacroHolder
from MacroBot.MacroEditor import MacroEditor
from MacroBot.Message import Message



class MacroCreator:
    __slots__ = ["__macros", "name"]
    __mode = ModeHolder()


    def __init__(self):
        self.__macros = MacroHolder()


    def has_macro(self) -> bool:
        return self.__macros.has_macro(self.name)


    def __defined(self) -> str:
        return "Macro \""+self.name+"\" defined successfully"
    def __deleted(self) -> str:
        return "Macro \""+self.name+"\" successfully deleted"

    def __predefined(self) -> str:
        return "Error: Macro \""+self.name+"\" has already been declared"
    def __undefined(self) -> str:
        return "Error: Macro \""+self.name+"\" has not yet been declared"


    def __add(self) -> str:
        if self.has_macro():
            return self.__predefined()
        
        self.__macros.add_macro(self.name)
        return self.__defined()
    def __del(self) -> str:
        if not self.has_macro():
            return self.__undefined()

        self.__macros.del_macro(self.name)
        return self.__deleted()
    def __edit(self) -> str:
        if not self.has_macro():
            return self.__undefined()

        self.__mode.set_mode("edit", self.name)
        return "Changed to edit mode"

    
    async def macro(self, message:Message):
        if len(message.words) != 3:
            await message.send("Error: Wrong number of arguments")
            return

        command = message.words[1]
        self.name = message.words[2]

        if command == "add":
            await message.send(self.__add())
            return

        if command == "del":
            await message.send(self.__del())
            return

        if command == "edit":
            await message.send(self.__edit())
            return


    async def edit(self, message:Message):
        macro = self.__macros.get_macro(self.__mode.get_mode("edit"))
        await MacroEditor(message, macro).edit()


    async def loop(self):
        await self.__macros.loop()
    async def message(self, message:Message):
        await self.__macros.message(message)
