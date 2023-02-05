from datetime import datetime


class ISODateConverter:
    """ Пользовательский конвертер маршрутов. """
    regex = r"\d{4}-\d{2}-\d{2}"  # захватываем часть строки формата YYYY-MM-DD

    def to_python(self, value: str):
        """ Метод обрабатывает захваченную регуляркой строку в python тип, который должен быть передан Django View. """
        return datetime.strptime(value, '%Y-%m-%d')
