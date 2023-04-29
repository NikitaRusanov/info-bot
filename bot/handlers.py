from telebot import TeleBot
from telebot.types import Message
from abc import ABC, abstractmethod
from typing import Optional
from bot.messages import BaseMessages, get_messages


class BaseHandler(ABC):
    '''Message handler interface'''
    def __int__(self):
        self.bot: Optional[TeleBot] = None
        self.messages: Optional[BaseMessages] = None

    def __call__(self, message: Message, bot: TeleBot) -> None:
        self.bot = bot
        self.messages = get_messages('regular')
        self.handle(message)

    @abstractmethod
    def handle(self, message: Message) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    def handle(self, message: Message) -> None:
        self.bot.reply_to(message, self.messages.start(message.from_user.first_name))


class HelpHandler(BaseHandler):
    def handle(self, message: Message) -> None:
        self.bot.reply_to(message, self.messages.help())


def setup_handlers(bot: TeleBot):
    bot.register_message_handler(callback=StartHandler(), commands=['start'], pass_bot=True)
    bot.register_message_handler(callback=HelpHandler(), commands=['help'], pass_bot=True)
