import telebot
import feed

token =''
rss_iran = "https://www.irinn.ir/fa/rss/allnews"
rss_bbc = "http://www.bbc.co.uk/persian/index.xml"


bot = telebot.TeleBot(token)


iran =feed.news(rss_iran)
bbc =feed.news(rss_bbc)

print (iran ,"\n", bbc)


@bot.message_handler(commands=['iran'])
def start_message(message):
    bot.send_message(message.chat.id, iran)
@bot.message_handler(commands=['bbc'])
def start_message(message):
    bot.send_message(message.chat.id, bbc)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/bbc', '/iran', '/start')
    bot.send_message(message.chat.id, 'fuck_nows', reply_markup=keyboard)
print ("ok")
bot.polling()
