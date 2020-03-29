import json
import codecs

from MacroBot.Macro import Macro

def save(macros):
    """
    macros: list[Macro]
    """
    save_datas: dict[dict] = {}
    
    for key, m in macros.items():
        if m.vars.vars["send_channel"] is None:
            channel_id = None
        else:
            channel_id = m.vars.vars["send_channel"].id
        macro:dict = {
            "event": m.event,
            "code" : m.code,
            "vars" : {
                "send_channel": channel_id,
                "send_content": m.vars.vars["send_content"]
            }
        }
        save_datas[key] = macro

    with codecs.open("MacroBot/data.json", "w", "utf-8") as f:
        json.dump(save_datas, f, ensure_ascii=False)

