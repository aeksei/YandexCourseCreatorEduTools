from datetime import timedelta

from django.views.generic import TemplateView


class OrdersListView(TemplateView):
    template_name = "orders/date.html"

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)  # kwargs будет содержать параметры из url, в данном случае date_orders

        # TODO с помощью timedelta получить предыдущую дату и следующую

        return context
