from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "これからバイト、大変だナ"

    def get_author(self):
        return "Miyajima"