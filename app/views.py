from django.shortcuts import render, reverse
from django.http import HttpResponse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)



content = os.listdir(path='.')

def show_time(request):
    today = datetime.datetime.today()
    date_time = today.strftime("%Y/%m/%d %H.%M.%S")
    return HttpResponse(date_time)

def show_workdir(request):
    return HttpResponse(content)


