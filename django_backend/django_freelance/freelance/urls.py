from django.urls import path  # стандартно - маршруты
from django.urls import include  # для расширения маршрутов из других приложений
from .views import *  # все представления из приложения

# список маршрутов
urlpatterns = [
    # путь('url'/, класс_представления.as_view()/функция представления, name='имя_маршрута'),
    path('tickets/all', TicketListView.as_view()),
]
