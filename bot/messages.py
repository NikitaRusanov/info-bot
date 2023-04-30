from abc import ABC, abstractmethod
from enum import Enum


class BaseMessages(ABC):
    @abstractmethod
    def start(self, username) -> str:
        raise NotImplemented

    @abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abstractmethod
    def ask_ticker(self) -> str:
        raise NotImplemented

    @abstractmethod
    def wrong_ticker(self) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):

    def wrong_ticker(self) -> str:
        return 'Вы ввели непраильный тикер акции'

    def ask_ticker(self) -> str:
        return 'Введите тикер акции, график которой хотите получить'

    def start(self, username) -> str:
        return f'Hello, {username}!'

    def help(self) -> str:
        return 'It is a bot, that can send you message, when stock reach some price'


def get_messages(user_role: str) -> BaseMessages:
    if user_role == 'regular':
        return RegularUser()
    raise ValueError
