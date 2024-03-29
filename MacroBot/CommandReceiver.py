from MacroBot.ModeHolder import ModeHolder
from MacroBot.Message import Message
from MacroBot.Saver import save


class CommandReceiver:
    __mode = ModeHolder()


    def __init__(self, message:Message):
        self.message = message
        self.command = self.message.words
        self.command[0] = self.command[0][1:]
    

    async def receive(self, macros):
        head = self.command[0]
        if head == "write":
            flag = not self.__mode.get_mode("write")
            self.__mode.set_mode("write", flag)
            text = "Changed to write mode" if flag else "Exited write mode"
            await self.message.send(text)
            return

        if head == "channel_id":
            await self.message.send(self.message.channel_id)

        if head == "user_id":
            await self.message.send(self.message.author_id)

        if head == "save":
            save(macros)
            await self.message.send("Data saved!")
