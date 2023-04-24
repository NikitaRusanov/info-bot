from telebot import TeleBot
from telebot.types import Message
from abc import ABC, abstractmethod
from typing import Optional


class BaseHandler(ABC):
    @abstractmethod
    def __call__(self, message: Message, bot: Optional[TeleBot]) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    def __call__(self, message: Message, bot: Optional[TeleBot]) -> None:
        bot.reply_to(message, 'It is a bot, that can send you message, when stock reach some price')


def setup_handlers(bot: TeleBot):
    bot.register_message_handler(callback=StartHandler(), commands=['help', 'start'], pass_bot=True)
