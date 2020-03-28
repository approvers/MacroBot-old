from MacroBot.Variables import Variables
from MacroBot.Message import Message



class Macro:
    def __init__(self):
        self.event = ""
        self.code = ""
        self.vars = Variables()
        self.globals = {}


    async def run(self):
        try:
            exec(self.code, self.globals, self.vars.vars)
            content = self.vars.vars["send_content"]
            channel = self.vars.vars["send_channel"]
            await channel.send(content)
        except Exception as E:
            print(str(type(E)) + str(E))

        self.globals = {}


    async def loop(self):
        if self.event != "loop":
            return
        
        await self.run()

    async def message(self, message:Message):
        if self.event != "message":
            return

        self.vars.vars["message"] = message
        self.globals["message"] = globals()["Message"]
        await self.run()