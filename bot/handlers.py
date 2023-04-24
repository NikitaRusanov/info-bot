from telebot import TeleBot
from telebot.types import Message
from abc import ABC, abstractmethod
from typing import Optional


class BaseHandler(ABC):
    def __int__(self):
        self.bot: Optional[TeleBot] = None

    def __call__(self, message: Message, bot: TeleBot) -> None:
        self.bot = bot
        self.handle(message)

    @abstractmethod
    def handle(self, message: Message) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    def handle(self, message: Message) -> None:
        self.bot.reply_to(message, f'Hello, {message.from_user.first_name}! It is a bot, that can send you message, when stock reach some price')


def setup_handlers(bot: TeleBot):
    bot.register_message_handler(callback=StartHandler(), commands=['help', 'start'], pass_bot=True)
