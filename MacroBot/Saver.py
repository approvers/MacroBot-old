import json

def saver(macros: dict[Macro]):
    """
    macros: list[Macro]
    """
    save_datas: dict[dict] = {}
    
    for key, m in macros.items():
        macro:dict = {
            "event": m.event,
            "code" : m.code,
            "vars" : {
                "channel_id": m.vars["send_channel"].id
                "send_content": m.vars["send_content"]
            }
        }
        save_datas[key] = macro

    json_string = json.dumps(save_datas, ensure_ascii=False, indent=2)
    with open("data.json", "w") as f:
        f.write(json_string.encode("utf-8"))

