from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    title = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:10]
    title = f'Посты сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
