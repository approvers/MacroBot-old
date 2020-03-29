# MacroBot
※大文字は任意の値

### 「！」で始まるコマンド
#### !write
writeモードに変更

#### !user_id
送信者のIDを表示

#### !channel_id
送信したチャンネルのIDを表示


### writeモードで使えるコマンド

#### macro add NAME
マクロ名「NAME」を宣言

#### macro del NAME
マクロ名「NAME」を削除

#### macro edit NAME
マクロ名「NAME」のeditモードに変更


### マクロのeditモードで使えるコマンド

#### event EVENT
マクロの発動イベントを「EVENT」に設定  
EVENTは"message"と"loop"が用意されている  
"loop"1分ごとに発動するが安全ではない

#### code CODE
マクロの発動時に実行されるコード（Python）を設定

#### var add NAME [VALUE]
変数NAMEを宣言しVALUE（文字列）を代入  
VALUEは指定しなくてもよい初期値はNone

#### var del NAME
変数NAMEを削除

#### var set NAME VALUE
変数NAMEにVALUEを代入

#### var get [NAME]
変数NAMEの値を表示
NAMEを指定しない場合は変数名を列挙する
