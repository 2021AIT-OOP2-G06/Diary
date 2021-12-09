from abc import ABC, abstractclassmethod, abstractmethod


class KabuDiary(ABC):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "足を引っ張らない様にやろうと思った。"

    def get_author(self):
        return "Kabura"
