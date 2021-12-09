from abc import ABC, abstractclassmethod, abstractmethod

class UchiyamaDiary(ABC):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "初めまして"

    def get_author(self):
        return "Uchiym"