from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# Открытие сайта -> функция index запускается, запрос от пользователя
def index(requests):
    return HttpResponse("Успешно")
