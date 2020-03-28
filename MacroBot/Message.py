import discord



class Message:
    def __init__(self, MESSAGE:discord.message):
        self.message:discord.message = MESSAGE
        self.author:discord.abc.User = self.message.author
        self.author_id:int = self.author.id
        self.content:str = self.message.content
        self.channel:discord.abc.Messageable = self.message.channel
        self.channel_id:int = self.channel.id
        self.words:list = self.content.split()

    
    def author_is_bot(self) -> bool:
        return self.author.bot
    def is_command(self) -> bool:
        return self.content.startswith("!")

    async def send(self, content=None):
        await self.channel.send(content)