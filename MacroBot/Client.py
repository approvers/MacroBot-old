from discord.ext import tasks
import discord
import os
import json

from MacroBot.Message import Message
from MacroBot.MessageReceiver import MessageReceiver



class Client(discord.Client):
    __TOKEN = os.environ["TOKEN"]
    
    def run(self):
        super().run(self.__TOKEN)

    async def on_ready(self):
        if not os.path.exists("MacroBot/data.json"):
            self.__receiver = MessageReceiver()
            self.macro_loop.start()
            return
        with open("MacroBot/data.json", encoding="utf-8") as f:
            data = json.load(f)
        for key, value in data.items():
            data[key]["vars"]["send_channel"] = self.get_channel(value["vars"]["send_channel"])
            data[key]["vars"]["message"] = None
        self.__receiver = MessageReceiver(data)
        self.macro_loop.start()

    async def on_message(self, message):
        await self.__receiver.receive(Message(message))

    @tasks.loop(seconds=60)
    async def macro_loop(self):
        await self.__receiver.loop()
