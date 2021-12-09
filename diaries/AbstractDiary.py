from abc import ABC, abstractclassmethod, abstractmethod
class AbstractDiary(ABC):
    @abstractmethod
    def get_date(sell):
        pass

    @abstractmethod
    def get_summary(self):
        pass
    
    @abstractmethod
    def get_author(self):
        pass