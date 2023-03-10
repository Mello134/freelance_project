from django.urls import path  # стандартно - маршруты
from django.urls import include  # для расширения маршрутов из других приложений
from .views import *  # все представления из приложения
from rest_framework.authtoken.views import obtain_auth_token  # для аутентификации


# список маршрутов
urlpatterns = [
    # маршруты для получения токенов аутентификации
    path('auth/', include('djoser.urls')),  # здесь urls джосера, для регистрации и авторизации
    path('auth/token', obtain_auth_token, name='token'),

    # путь('url'/, класс_представления.as_view()/функция представления, name='имя_маршрута'),
    path('executors/<int:pk>/', ExecutorRetrieveView.as_view()),  # Получаем исполнителя по pk
    path('executors/update/<int:pk>/', ExecutorUpdateView.as_view()),  # Обновляем исполнителя по pk
    path('executors/new/', ExecutorCreateView.as_view()),  # Создаём исполнителя
    path('executors/all/', ExecutorListView.as_view()),  # Получаем список исполнителей

    path('customers/<int:pk>/', CustomerRetrieveView.as_view()),  # Получаем заказчика по pk
    path('customers/update/<int:pk>/', CustomerUpdateView.as_view()),  # Обновляем заказчика по pk
    path('customers/new/', CustomerCreateView.as_view()),  # Создаём заказчика
    path('customers/all/', CustomerListView.as_view()),  # Получаем список заказчиков

    path('orders/<int:pk>/', OrderRetrieveView.as_view()),  # Получаем заказа по pk
    path('orders/update/<int:pk>/', OrderUpdateView.as_view()),  # Обновляем заказ по pk
    path('orders/new/', OrderCreateView.as_view()),  # Создаём заказ
    path('orders/all/', OrderListView.as_view()),  # Получаем список заказов

    path('services/<int:pk>/', ServiceRetrieveView.as_view()),  # Получаем услугу по pk
    path('services/update/<int:pk>/', ServiceUpdateView.as_view()),  # Обновляем услугу по pk
    path('services/new/', ServiceCreateView.as_view()),  # Создаём услугу
    path('services/all/', ServiceListView.as_view()),  # Получаем список услуг

    path('tags/<int:pk>/', TagRetrieveView.as_view()),  # Получаем тег по pk
    path('tags/update/<int:pk>/', TagUpdateView.as_view()),  # Обновляем тег по pk
    path('tags/new/', TagCreateView.as_view()),  # Создаём тег
    path('tags/all/', TagListView.as_view()),  # Получаем список тегов

    path('orderings/<int:pk>/', OrderingRetrieveView.as_view()),  # Получаем определённого заказа по pk
    path('orderings/update/<int:pk>/', OrderingUpdateView.as_view()),  # Обновляем определённого заказа по pk
    path('orderings/new/', OrderingCreateView.as_view()),  # Создаём определённого заказа
    path('orderings/all/', OrderingListView.as_view()),  # Получаем список определённых заказов

    path('messages/<int:pk>/', MessageRetrieveView.as_view()),  # Получаем Сообщение по pk
    path('messages/update/<int:pk>/', MessageUpdateView.as_view()),  # Обновляем Сообщение по pk
    path('messages/new/', MessageCreateView.as_view()),  # Создаём Сообщение
    path('messages/all/', MessageListView.as_view()),  # Получаем список Сообщений

    path('tickets/<int:pk>/', TicketRetrieveView.as_view()),  # Получаем Тикет по pk
    path('tickets/update/<int:pk>/', TicketUpdateView.as_view()),  # Обновляем Тикет по pk
    path('tickets/new/', TicketCreateView.as_view()),  # Создаём Тикет
    path('tickets/all/', TicketListView.as_view()),  # Получаем список Тикетов

    path('authorings/<int:pk>/', AuthoringRetrieveView.as_view()),  # Получаем Автора_ревью по pk
    path('authorings/update/<int:pk>/', AuthoringUpdateView.as_view()),  # Обновляем Автора_ревью по pk
    path('authorings/new/', AuthoringCreateView.as_view()),  # Создаём Автора_ревью
    path('authorings/all/', AuthoringListView.as_view()),  # Получаем список Авторов_ревью

    path('reviews/<int:pk>/', ReviewRetrieveUpdateView.as_view()),  # Получаем Ревью по pk
    path('reviews/update/<int:pk>/', ReviewRetrieveUpdateView.as_view()),  # Обновляем Ревью по pk
    path('reviews/new/', ReviewCreateView.as_view()),  # Создаём Ревью
    path('reviews/all/', ReviewListView.as_view()),  # Получаем список Ревью
]
