from telebot import TeleBot
from config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def start_message(message):
    bot.reply_to(message, 'It is a bot, that can send you message, when stock reach some price')


bot.infinity_polling()