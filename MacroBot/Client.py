import discord
import os

from MacroBot.Message import Message
from MacroBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]
    __receiver = MessageReceiver()
    
    
    def run(self):
        super().run(self.__TOKEN)


    async def on_ready(self):
        pass


    async def on_message(self, message):
        await self.__receiver.receive(Message(message))


    async def macro_loop(self):
        await self.__receiver.loop()