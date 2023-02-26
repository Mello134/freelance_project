from django.contrib import admin
from .models import *  # импорт всех моделей

# Регистрируем все модели
admin.site.register(Customer)
admin.site.register(Executor)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Ordering)
admin.site.register(Message)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(Authoring)
