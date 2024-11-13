import copy
from lib2to3.fixes.fix_input import context
from pydoc import pager
from tkinter.messagebox import QUESTION

from django.contrib.admin.templatetags.admin_list import pagination
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse, Http404
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(1, 30)
]


ANSWERS = [
    {
        'answer': f'Answer {i}',
        'user_avatar': '/img/вумен_лягушка.jpg'
    } for i in range(1, 4)
]


def pagination(objects_list, request, per_page=10):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, per_page)
    try:
        page = paginator.page(page_num)
    except InvalidPage:
        raise Http404("Страница не найдена")
    return page


def index(request):
    page = pagination(QUESTIONS, request, 5)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page})


def question(request, question_id):
    question = QUESTIONS[question_id - 1]
    return render(request, 'question.html', context={'question': question, 'answers': ANSWERS})


def hot(request):
    page = pagination(QUESTIONS, request, 5)
    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page})


def tag(request, tag_name):
    page = pagination(QUESTIONS, request, 5)
    return render(request, 'tag.html', context={'questions': page.object_list, 'tag_name': tag_name, 'page_obj': page})


def settings(request):
    return render(request, 'setting.html')


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
