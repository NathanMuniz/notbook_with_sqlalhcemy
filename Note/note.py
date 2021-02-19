from datetime import date
current_date = date.today()

class Note():
    def __init__(self, title, memo, tags):
        self.__title = title
        self.__memo = memo
        self.__tags = tags
        self.__create_date = current_date

    @property
    def title(self):
        return self.__title

    @property
    def memo(self):
        return self.__memo

    @property
    def tags(self):
        return self.__tags

    @property
    def current_date(self):
        return self.__create_date

    def show_dates(self):
        return f"id: 1, Title: {self.__title}, Data: {self.__create_date}\n" \
        f"Memo: {self.__memo}\n" \
        f"tags: {self.__tags}"


