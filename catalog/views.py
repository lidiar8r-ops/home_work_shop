from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    # Выбираем последние 5 созданных продуктов (по полю created_at)
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим в консоль (для отладки)
    for product in latest_products:
        print(f"Продукт: {product.name}, Цена: {product.price}, Дата: {product.created_at}")

    context = {
        'latest_products': latest_products
    }
    return render(request, 'home.html', context)


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
