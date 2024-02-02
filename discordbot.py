############################################################################
#                            BOTのメインプログラム                          #
############################################################################

import discord
import cmdfunc
import mytool

#DiscordBOTのトークン
TOKEN = 'ここにトークン'

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# コマンドテーブル　[コマンド,関数名]
cmd_func_table = [
    ["/test",cmdfunc.test],
]
TBL_CMD = 0
TBL_FUNC = 1

# 動作する処理
@client.event
async def on_ready():
    print('起動')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    # コマンドを空白文字区切りで分割
    div_message = mytool.cmd_div(message)

    # コマンドテーブルに登録されているコマンドに応じて処理
    for i in range(len(cmd_func_table)):
        if div_message[0] == cmd_func_table[i][TBL_CMD]:
            await cmd_func_table[i][TBL_FUNC](message,client,div_message)
            return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)






