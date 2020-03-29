import json
import codecs

from MacroBot.Macro import Macro

def saver(macros):
    """
    macros: list[Macro]
    """
    save_datas: dict[dict] = {}
    
    for key, m in macros.items():
        macro:dict = {
            "event": m.event,
            "code" : m.code,
            "vars" : {
                "channel_id": m.vars["send_channel"].id,
                "send_content": m.vars["send_content"]
            }
        }
        save_datas[key] = macro

    with codecs.open("MacroBot/data.json", "w", "utf-8") as f:
        json.dump(save_datas, f, ensure_ascii=False)

