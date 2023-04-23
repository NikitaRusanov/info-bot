from telebot import TeleBot
from telebot.types import Message


def start_command(message: Message, bot: TeleBot):
    bot.reply_to(message, 'It is a bot, that can send you message, when stock reach some price')


def setup_handlers(bot: TeleBot):
    bot.message_handler(commands=['start', 'help'], func=start_command)
