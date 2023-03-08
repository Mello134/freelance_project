# from django.shortcuts import render  # обычный render не используется в DRF

from rest_framework.response import Response  # для создания ответа
from rest_framework import generics

# импорт всех моделей и сериализаторов
from .models import *
from .serializers import *

from rest_framework.views import APIView


#____________________________________________________________________________________________
# API представление Исполнителя - получить по pk
class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


# API представление Исполнителя для обновления данных (по pk)
class ExecutorUpdateView(generics.UpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


# API представление Исполнителя для создания записи (по pk)
class ExecutorCreateView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


# API представление для списка Исполнителей
class ExecutorListView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
#____________________________________________________________________________________________


# API представление Заказчика - получить по pk
class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# API представление Заказчика для обновления данных (по pk)
class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


# API представление Заказчика для создания записи (по pk)
class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


# API представление для списка Заказчиков
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# API представление Заказа - получить по pk
class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# API представление Заказа для обновления данных (по pk)
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


# API представление Заказа для создания записи (по pk)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


# API представление для списка Заказов
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# API представление Услуги - получить по pk
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# API представление Услуги для обновления данных (по pk)
class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer


# API представление Услуги для создания записи (по pk)
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer


# API представление для списка Услуг
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# API представление Тега - получить по pk
class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# API представление Тега для обновления данных (по pk)
class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


# API представление Тега для создания записи (по pk)
class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


# API представление для списка Тегов
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# API представление определённого заказа - получить по pk
class OrderingRetrieveView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


# API представление определённого заказа для обновления данных (по pk)
class OrderingUpdateView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer


# API представление определённого заказа для создания записи (по pk)
class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer


# API представление для списка определённого заказов
class OrderingListView(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


# API представление Сообщения - получить по pk
class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# API представление Сообщения для обновления данных (по pk)
class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


# API представление Сообщения для создания записи (по pk)
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


# API представление для списка Сообщений
class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# API представление Тикета - получить по pk
class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# API представление Тикета для обновления данных (по pk)
class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer


# API представление Тикета для создания записи (по pk)
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer


# API представление для списка Тикетов
class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# API представление Автора_ревью - получить по pk
class AuthoringRetrieveView(generics.RetrieveAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


# API представление Автора_ревью для обновления данных (по pk)
class AuthoringUpdateView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer


# API представление Автора_ревью для создания записи (по pk)
class AuthoringCreateView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer


# API представление для списка Авторов_ревью
class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


# API - Ревью, получение по pk + обновление
class ReviewRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# API - Ревью, создание
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# API - список Ревью
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



# пример высокооуровневого API view
# # # ListAPIView - базовый клас представления DRF
# class TicketListView(generics.ListAPIView):
#     queryset = Ticket.objects.all()  # все объекты модели
#     serializer_class = TicketSerializer  # сериализатор для модели


# # пример низкоуровневого API view
# class TicketListView(APIView):
#     # самостоятельно указываем метод get
#     def get(self, request):
#         # самостоятельно указываем queryset (записи модели Ticket)
#         queryset = Ticket.objects.all()
#         # указываем сериализатор
#         # serializer_class = Сериализатор(данные_из_бд, в_модели_много_записей_т.е_список)
#         serializer_class = TicketSerializer(queryset, many=True)
#
#         # вернуть Ответ (данные сериализатора)
#         return Response({'tickers': serializer_class.data})
