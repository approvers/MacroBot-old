from MacroBot.ModeHolder import ModeHolder
from MacroBot.Message import Message
from MacroBot.Macro import Macro



class MacroEditor:
    __slots__ = ["message", "macro", "args"]
    __mode = ModeHolder()


    def __init__(self, message:Message, macro:Macro):
        self.message = message
        self.macro = macro


    def __exit(self) -> str:
        self.__mode.set_mode("edit", None)
        return "Exited edit mode"
    def __event(self) -> str:
        if len(self.message.words) == 1:
            return "```python\n"+self.macro.event+"\n```"

        self.macro.event = " ".join(self.message.words[1:])
        return "Event changed successfully"
    def __code(self) -> str:
        if len(self.message.words) == 1:
            return "```python\n"+self.macro.code+"\n```"

        self.macro.code = self.message.content[5:]
        return "Code changed successfully"
    def __var(self) -> str:
        return self.macro.vars.var(self.message)


    async def edit(self):
        command = self.message.words[0]

        if command == "exit":
            await self.message.send(self.__exit())
            return

        if command == "event":
            await self.message.send(self.__event())
            return

        if command == "code":
            await self.message.send(self.__code())
            return

        if command == "var":
            await self.message.send(self.__var())
            return
