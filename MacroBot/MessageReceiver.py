from MacroBot.Message import Message
from MacroBot.ModeHolder import ModeHolder
from MacroBot.MacroCreator import MacroCreator
from MacroBot.CommandReceiver import CommandReceiver



class MessageReceiver:
    __mode = ModeHolder()


    def __init__(self, data={}):
        self.creator = MacroCreator(data)

    async def receive(self, message:Message):
        if message.author_is_bot():
            return

        if message.is_command():
            await CommandReceiver(message).receive(self.creator.macros.macros)
            return
        
        await self.creator.message(message)


        if not self.__mode.get_mode("write"):
            return

        if self.__mode.get_mode("edit") is not None:
            await self.creator.edit(message)
            return

        if message.words[0] == "macro":
            await self.creator.macro(message)
            return

    
    async def loop(self):
        await self.creator.loop()
