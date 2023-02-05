from datetime import datetime

from django.http import HttpResponse
from django.views import View


class OrdersListView(View):
    def get(self, request):  # TODO метод должен дополнительно принимать дату
        date_format_with_month_name = ...  # TODO запишите формат даты, в котором месяц будет записан словом
        date_month_name = ...  # TODO преобразуйте объект datetime в строку соответствующего формата

        return HttpResponse(date_month_name)
