from discord.ext import tasks

from MacroBot.Client import Client


client = Client()


@tasks.loop(seconds=60)
async def loop():
    await client.macro_loop()


loop.start()
client.run()