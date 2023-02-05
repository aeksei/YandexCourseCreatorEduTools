from datetime import datetime


class ISODateConverter:
    """ Пользовательский конвертер маршрутов. """
    regex = r"\d{4}-\d{2}-\d{2}"  # захватываем часть строки формата YYYY-MM-DD
    date_format = '%Y-%m-%d'

    def to_python(self, value: str):
        """ Метод обрабатывает захваченную регуляркой строку в python тип, который должен быть передан Django View. """
        return datetime.strptime(value, self.date_format)

    def to_url(self, value: datetime):
        """ Метод обрабатывает python тип, и возвращает строку, которая будет подставлена в url. """
        return value.strftime(self.date_format)
