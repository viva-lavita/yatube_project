from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Посты отфильтрованные по группам {slug}')

# Create your views here.
