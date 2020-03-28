from MacroBot.Singleton import Singleton



class ModeHolder(Singleton):
    def set_up(self):
        self.__mode = {
            "write":False,
            "edit":None
        }

        

    def set_mode(self, mode_name:str, value):
        self.__mode[mode_name] = value

    def get_mode(self, mode_name:str):
        return self.__mode[mode_name]