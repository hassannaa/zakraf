import requests
from telebot import types
import telebot
from time import sleep
import random
import marshal  

token = input("5569138339:AAFPifJL8KvfHAjwIjyVx6EzMMlGrwWvPmw")
bot = telebot.TeleBot(token)
r=requests.session() 

trk = types.InlineKeyboardButton(text="- XDev ",url="https://t.me/Lq_bc")


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 4
    maac.add(trk)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في بوت الزخرفة
الان قم بأرسال اسمك ليتم زخرفتة. 
- - - - - - - - - - 
By  : @lq_bc 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)

@bot.message_handler(func=lambda m:True ) 
def com(message):
    msg=message.text 
    s = msg
    url = requests.get(f"https://v6vv.tk/API/Decorations-text.php?type=ar&text={s}").text
    print(url)
    bot.send_message(message.chat.id,f"Done ✅:\n{url}",parse_mode="markdown")
bot.polling(True)