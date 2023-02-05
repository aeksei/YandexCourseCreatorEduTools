from django.urls import path, register_converter

from orders import views, converters

register_converter(converters.ISODateConverter, 'date_iso')


urlpatterns = [
    path('orders/<date_iso:date_orders>/', views.OrdersListView.as_view()),  # TODO добавить в path аргумент name
]
