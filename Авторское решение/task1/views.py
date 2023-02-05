from datetime import datetime

from django.http import HttpResponse
from django.views import View


class OrdersListView(View):
    def get(self, request, date_orders: datetime):
        date_format_with_month_name = "%d %B %Y"
        date_month_name = date_orders.strftime(date_format_with_month_name)

        return HttpResponse(date_month_name)
