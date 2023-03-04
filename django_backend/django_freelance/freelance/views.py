# from django.shortcuts import render  # обычный render не используется в DRF

from rest_framework.response import Response  # для создания ответа
from rest_framework import generics

# импорт всех моделей и сериализаторов
from .models import *
from .serializers import *


# представление для тикетов
# ListAPIView - базовый клас представления DRF
class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()  # все объекты модели
    serializer_class = TicketSerializer  # сериализатор для модели
