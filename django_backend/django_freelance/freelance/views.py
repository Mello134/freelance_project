# from django.shortcuts import render  # обычный render не используется в DRF

from rest_framework.response import Response  # для создания ответа
from rest_framework import generics
from rest_framework import permissions, status  # проверка авторизованности

# импорт всех моделей и сериализаторов
from .models import *
from .serializers import *

from rest_framework.views import APIView


# представление Logout
class Logout(APIView):
    """ Будем получать пользователя, и из его данных удаляем токен, возвращаем статус 200"""
    def get(self, request, format=None):
        request.user.auth_token.delete()  # удаляем токен
        return Response(status=status.HTTP_200_OK)  # Отвечаем - 200 OK


#____________________________________________________________________________________________
# API представление Исполнителя - получить по pk
class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


# API представление Исполнителя для обновления данных (по pk)
class ExecutorUpdateView(generics.UpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Заказа для создания записи (по pk)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление для списка Заказов
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    # переопределяю queryset (фильтр)
    def get_queryset(self):
        queryset = Order.objects.all()  # весь список
        params = self.request.query_params  # параметры request

        order_type = params.get('order', None)  # ?order=1
        price = params.get('price', None)  # ?price=3000
        customer = params.get('customer', None)  # ?customer=pk/id

        # проверяем в адресной строке '?order=...'
        if order_type:
            # если записи есть применяем фильтр
            # queryset.filter(поле_модели=вышеуказанная_переменная)
            queryset = queryset.filter(order_type=order_type)

        # фильтр по цене
        if price:
            # lte - это меньше или равно (<=)
            queryset = queryset.filter(price__lte=price)

        # фильтр по заказчику
        if customer:
            # executor__id - Service (ForeignKey) --> Customer ->pd/id
            queryset = queryset.filter(customer__id=customer)

        # обязательно возвращаем queryset
        return queryset


# API представление Услуги - получить по pk
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# API представление Услуги для обновления данных (по pk)
class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Услуги для создания записи (по pk)
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление для списка Услуг
class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    # переопределяю queryset (фильтр)
    def get_queryset(self):
        # изначально беру все записи, будут выводить если фильтры не используются
        queryset = Service.objects.all()
        # params - своя переменная. В неё запишем все параметры, что получаем из request
        params = self.request.query_params

        # """ Буду фильтровать по полям service_type, price, executor"""
        # Переменной service_type - присваиваем то, что написано в браузерной строке, то есть в гет запросе
        # т.е. если в адресной строке будет написано service(это ключи)=значение, если ничего присвоим просто None
        service_type = params.get('service', None)
        price = params.get('price', None)
        executor = params.get('executor', None)

        # проверяем, написано ли что-то в адресной строке, связанное с service_type
        if service_type:
            # если написано, фильтруем по полю service_type - изменяем queryset, добавив фильтр
            # queryset.filter(поле_в_модели=переменная_в_текущем_представлении)
            queryset = queryset.filter(service_type=service_type)

        # фильтр по цене
        if price:
            # lte - это меньше или равно (<=)
            queryset = queryset.filter(price__lte=price)

        # фильтр по исполнителю
        if executor:
            # executor__id - это обращение к модели Executor к полю id, через текущую модель Service (ForeignKey)
            queryset = queryset.filter(executor__id=executor)

        # обязательно возвращаем queryset
        return queryset


# API представление Тега - получить по pk
class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# API представление Тега для обновления данных (по pk)
class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Тега для создания записи (по pk)
class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление определённого заказа для создания записи (по pk)
class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Сообщения для создания записи (по pk)
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление для списка Сообщений
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    # переопределяю queryset (фильтр)
    def get_queryset(self):
        queryset = Message.objects.all()  # весь список

        params = self.request.query_params

        # None - это default=None
        executor = params.get('executor', None)  # фильтр по исполнителю
        customer = params.get('customer', None)  # фильтр по заказчику
        from_date = params.get('from_date', None)  # фильтр по дате сообщений (от)
        to_date = params.get('to_date', None)  # фильтр по дате сообщений (до)

        # применяем фильтры, если в адресной строке есть совпадения
        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        if from_date:
            # msg_date - поле модели Message
            # msg_date__gte - >=, т.е msg_date >= from_date (фильтр от даты)
            queryset = queryset.filter(msg_date__gte=from_date)

        if to_date:
            # msg_date__lte - <=, т.е msg_date >= to_date (фильтр до даты)
            queryset = queryset.filter(msg_gate__lte=to_date)

        return queryset


# API представление Тикета - получить по pk
class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# API представление Тикета для обновления данных (по pk)
class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Тикета для создания записи (по pk)
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление Автора_ревью для создания записи (по pk)
class AuthoringCreateView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API представление для списка Авторов_ревью
class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


# API - Ревью, получение по pk + обновление
class ReviewRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


# API - Ревью, создание
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # тип пользователя - авторизован или только для чтения
    permission_class = permissions.IsAuthenticatedOrReadOnly


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
