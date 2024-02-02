############################################################################
#                            自分で使う便利そうな関数                        #
############################################################################

import re

##
# メッセージを空白区切りで分割する
##
def cmd_div(message):
    div_message = message.content.split(" ")
    return div_message

##
# 文字列から数値のみ抽出
##
def str_to_num(str):
    val = re.sub(r"\D","",str) 
    return val
