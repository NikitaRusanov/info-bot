from telebot import TeleBot
from config import BOT_TOKEN
from bot.handlers import setup_handlers


def main():
    bot = TeleBot(BOT_TOKEN)
    setup_handlers(bot)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
