# HW1
from django.http import HttpResponse


def main(request):
    return HttpResponse("Начальная страница проекта")


def blogs(request):
    return HttpResponse("Тут будут блоги!")


def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")


def blog_detail(request, name=''):
    return HttpResponse(f'Здесь будет блог, вызываемый динамически, например: {name}')


def add_comment_to_post(request, name=''):
    return HttpResponse(f'{name} - это динамическая часть URL-адреса, которая будет '
                        f'использоваться для получения соответствующего поста из базы данных')


def create(request):
    return HttpResponse("Форма создания публикации")


def blog_update(request, name=''):
    return HttpResponse("Обновление существующего поста")


def blog_delete(request, name=''):
    return HttpResponse("Удаление существующего поста")


def profile(request, username=''):
    return HttpResponse(f'Персональная страница пользователя: {username}.')


def change_password(request, username=''):
    return HttpResponse(f'Изменение личных данных рользователя {username}.')


def register(request):
    return HttpResponse('Регистрация нового пользователя')


def login(request):
    return HttpResponse('Страница с формой для логина')
