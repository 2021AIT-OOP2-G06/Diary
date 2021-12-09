from abc import ABC, abstractclassmethod, abstractmethod

class IwaoDiary(ABC):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "みんなでグループワークがんばりたいと思った。"

    def get_author(self):
        return "Iwao"
