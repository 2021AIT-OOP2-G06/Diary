from diaries.AbstractDiary import AbstractDiary


class NodaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-01"

    def get_summary(self):
        return "今日誕生日だった"

    def get_author(self):
        return "Noda"
