from django.db import models
from django.contrib.auth.models import User


# Модель Исполнителя
class Executor(models.Model):
    # Связь со встроенной моделью User,
    # CASCADE - при удалении пользователя, из таблицы Executor, удалятся все записи с его участием
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # телефон, максимально 11 символов
    phone = models.CharField(max_length=11)

    # краткое отображения, для отдельной записи таблицы Executor
    def __str__(self):
        return "Пользователь(исп) {}, телефон: {}".format(self.user, self.phone)


# модель Заказчика - все поля аналогичны модели исполнителя
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "Пользователь(зак) {}, телефон: {}".format(self.user, self.phone)


# Модель Услуги (связь с исполнителем)
class Service(models.Model):
    # ЧОЙСЫ УСЛУГ (типы услуг)
    SERVICE_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография'),
    ]

    # Услуга связана с исполнителем (модель Executor) / Удалился исполнитель, удалится и его услуги
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    # Имя услуги
    name = models.CharField(max_length=250)
    # Описание услуги
    desc = models.CharField(max_length=1000)
    # цена услуги
    price = models.IntegerField()
    # Тип услуги, стандартно 1, макс длина 1
    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        # ВАЖНО self.get_service_type_display - чтобы отображалось именно название чойса, а не цифры от 1 до 7
        return "{}, {}, цена: {}".format(self.name, self.get_service_type_display(), self.price)


# Модель Заказ (связь с заказчиком)
class Order(models.Model):
    # ЧОЙСЫ УСЛУГ (типы услуг)
    ORDER_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    order_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        # ВАЖНО self.get_order_type_display - чтобы отображалось именно название чойса, а не цифры от 1 до 7
        return "{}, {}, цена: {}".format(self.name, self.get_order_type_display(), self.price)


# таблица опциональных ключей, тегов (Связи между услугами и заказами)
class Tag(models.Model):
    # связь с услугой
    # blank=True, null=True, не обязательное заполнение, поле может быть пустым, и разрешается null
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    # связь с заказом
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    # имя тега
    name = models.CharField(max_length=30)


# таблица определённого заказа
# (Связи между исполнителем и заказчиком + заказом и услугой)
class Ordering(models.Model):
    # связь с заказчиком
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # связь с исполнителем
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    # связь с услугой
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    # связь с заказом
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    # дата время
    order_date = models.DateTimeField()
    # дедлайн
    deadline = models.DateTimeField()

    def __str__(self):
        return "{} - {}, Исполнитель: {}, Заказчик: {}".format(self.order_date, self.deadline,
                                                               self.customer, self.executor)


# модель сообщений
class Message(models.Model):
    # заказчик
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # исполнитель
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    # дата сообщения
    msg_date = models.DateTimeField()
    # редактировалось ли сообщение
    is_edited = models.BooleanField(default=False)
    # текст сообщения
    desc = models.CharField(max_length=1000)


# тикеты (для общения с техподдержной сайта)
class Ticket(models.Model):
    # Чойсы на строгость, претензии
    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая'),
    ]

    # заказчик (опционально)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    # исполнитель (опционально)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    # оценка, чойс
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    # описание претензии
    desc = models.CharField(max_length=1000)
    # дата обращения, претензии
    ticket_date = models.DateTimeField()
    # статус обращения (решён / не решен)
    is_resolved = models.BooleanField(default=False)


# таблица Ревью (рейтинг)
class Review(models.Model):
    # Чойсы рейтинга
    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]

    # рейтинг
    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    # комментарий
    desc = models.CharField(max_length=1000)


# таблица автора ревью
class Authoring(models.Model):
    # связь с ревью
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    # автор ревью
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # опционально заказчик
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    # опционально исполнитель
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    # дата оценки
    review_date = models.DateTimeField()

    def __str__(self):
        return "{}, {}".format(self.author, self.review_date)
