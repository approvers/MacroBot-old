from MacroBot.Message import Message



class Variables:
    def __init__(self):
        self.vars = {
            "send_content":None,
            "send_channel":None,
            "message":None
        }

    
    def has_var(self):
        return self.name in self.vars.keys()


    def __defined(self) -> str:
        return "Variable \""+self.name+"\" defined successfully"
    def __deleted(self) -> str:
        return "Variable \""+self.name+"\" successfully deleted"
    def __definition(self) -> str:
        return "Variable \""+self.name+"\" = " + str(self.vars[self.name])

    def __predefined(self) -> str:
        return "Error: Variable \""+self.name+"\" has already been declared"
    def __undefined(self) -> str:
        return "Error: Variable \""+self.name+"\" has not yet been declared"


    def __add(self) -> str:
        if self.name is None:
            return "Error: Wrong number of arguments"

        if self.has_var():
            return self.__predefined()
            
        self.vars[self.name] = self.value
        return self.__defined()
    def __del(self) -> str:
        if self.name is None:
            return "Error: Wrong number of arguments"
        if self.value is not None:
            return "Error: Wrong number of arguments"

        if not self.has_var():
            return self.__undefined()

        del self.vars[self.name]
        return self.__deleted()
    def __set(self) -> str:
        if self.name is None:
            return "Error: Wrong number of arguments"
        if self.value is None:
            return "Error: Wrong number of arguments"

        if not self.has_var():
            return self.__undefined()

        self.vars[self.name] = self.value
        return self.__definition()
    def __get(self) -> str:
        if self.name is None:
            ans = self.vars.keys()
            return " ".join(ans)

        if not self.has_var():
            return self.__undefined()
            
        return self.__definition()
        

    def var(self, message) -> str:
        if len(message.words) < 2:
            return "Error: Wrong number of arguments"

        command = message.words[1]
        self.name = None
        self.value = None
        if len(message.words) >= 3:
            self.name = message.words[2]
        if len(message.words) == 4:
            self.value = " ".join(message.words[3:])

        if command == "add":
            return self.__add()

        if command == "del":
            return self.__del()

        if command == "set":
            return self.__set()

        if command == "get":
            return self.__get()