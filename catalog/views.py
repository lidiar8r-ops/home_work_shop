from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # print(name)
        # print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name} (тел. {phone})! Ваше сообщение {message} получено.")
    return render(request, "contacts.html")
