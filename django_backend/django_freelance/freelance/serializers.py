from rest_framework import serializers
from .models import *  # импортирую все модели
from django.contrib.auth.models import User  # импорт стандартной модели User


# # пример сериалайзера по типу моделей
# class User(serializers.Serializer):
#     # ниже поля которые будем передавать в JSON формате
#     user = serializers.CharField()
#     email = serializers.EmailField()


# сериализатор пользователя, модель User
class UserSerializer(serializers.ModelSerializer):
    # класс мета, уточняем данные к модели
    class Meta:
        model = User  # привязываем модель к сериализатору
        # какие поля модели нужно сериализовать
        fields = ['username', 'email', 'first_name', 'last_name']


# сериализатор модели исполнителя - Executor
class ExecutorSerializer(serializers.ModelSerializer):
    # создаём переменную в которой будет храниться вся информация о пользователе, а не только id
    # т.е, переменная user = сериализатору UserSerializer
    user = UserSerializer()

    class Meta:  # уточняем данные
        model = Executor  # привязываемся к модели Executor
        fields = '__all__'  # все поля модели


# сериализатор модели заказчика - Customer
class CustomerSerializer(serializers.ModelSerializer):
    # создаём переменную в которой будет храниться вся информация о пользователе, а не только id
    # т.е, переменная user = сериализатору UserSerializer
    user = UserSerializer()

    class Meta:  # уточняем данные
        model = Customer  # привязываемся к модели Customer
        fields = '__all__'  # все поля модели


# Делаю отдельный сериализатор для исполнителя, где не будет инфы о User
# он нужен когда пользователь ещё не зарегистрирован, то есть при создании
class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


# Делаю отдельный сериализатор для заказчика, где не будет инфы о User
# он нужен когда пользователь ещё не зарегистрирован, то есть при создании
class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# сериализатор для Услуги - модель Service
# Модель Услуги (связь с исполнителем)
class ServiceSerializer(serializers.ModelSerializer):
    # JSON данные об исполнителе
    executor = ExecutorSerializer()
    # ВАЖНО - для отображения чойса, а не просто номера чойса - сразу в JSON формате
    service_type = serializers.CharField(source='get_service_type_display')

    class Meta:
        model = Service
        fields = '__all__'


# сериализатор для Услуги - модель Service
# при создании/корректировании услуги
class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


# сериализатор для Заказа - модель Order
# Модель Услуги (связь с исполнителем)
class OrderSerializer(serializers.ModelSerializer):
    # JSON данные о заказчике
    customer = CustomerSerializer()
    # ВАЖНО - для отображения чойса, а не просто номера чойса - сразу в JSON формате
    order_type = serializers.CharField(source='get_order_type_display')

    class Meta:
        model = Order
        fields = '__all__'


# сериализатор для Заказа - модель Order
# при создании/корректировании заказ
class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# сериализатор для тегов - модель Tag (связи услуги и заказа)
# Модель Услуги (связь с исполнителем)
class TagSerializer(serializers.ModelSerializer):
    # JSON данные об услуге и заказе
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


# сериализатор для Tag - модель Tag
# при создании/корректировании Tag
class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# Сериализатор для модели Ordering - (Связи между исполнителем и заказчиком + заказом и услугой)
# У модели 4 ForeignKey поля, 2 из них опциональные
class OrderingSerializer(serializers.ModelSerializer):
    # JSON данные об исполнителе и заказчике + услуге и заказе
    service = ServiceSerializer()
    order = OrderSerializer()
    customer = CustomerSerializer()
    executor = ExecutorSerializer()

    class Meta:
        model = Ordering
        fields = '__all__'


# Сериализатор для модели Ordering - (Связи между исполнителем и заказчиком + заказом и услугой)
# При создании и редактировании
class CreateOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = '__all__'


# Сериализатор для модели Message - (Сообщения)
class MessageSerializer(serializers.ModelSerializer):
    # JSON данные об исполнителе и заказчике
    customer = CustomerSerializer()
    executor = ExecutorSerializer()

    class Meta:
        model = Message
        fields = '__all__'


# Сериализатор для модели Message - (Сообщения)
# При создании и редактировании
class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


# Сериализатор для модели Ticket - (для общения с техподдержной сайта)
class TicketSerializer(serializers.ModelSerializer):
    # JSON данные об исполнителе и заказчике
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    # ВАЖНО - для отображения чойса, а не просто номера чойса - сразу в JSON формате
    severity = serializers.CharField(source='get_severity_display')

    class Meta:
        model = Ticket
        fields = '__all__'


# Сериализатор для модели Ticket - (для общения с техподдержной сайта)
# При создании и редактировании
class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


# Сериализатор для модели Review - (оценки)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Сериализатор для модели Authoring - (автора ревью)
class AuthoringSerializer(serializers.ModelSerializer):
    # JSON данные об исполнителе и заказчике, о пользователе, об оценке
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    author = UserSerializer()
    review = ReviewSerializer()

    class Meta:
        model = Authoring
        fields = '__all__'


# Сериализатор для модели Authoring - (автора ревью)
# При создании и редактировании
class CreateAuthoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authoring
        fields = '__all__'
