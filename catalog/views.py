
from .models import Product

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

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
    """
    Обработка GET и POST запросов для страницы контактов.
    При успешной отправке формы — перенаправление на ту же страницу с сообщением.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and phone and message:
            # Здесь можно добавить логику сохранения/отправки
            messages.success(request, 'Сообщение отправлено!')
            return redirect('catalog:contacts')
        else:
            messages.error(request, 'Заполните все поля!')

    # Для GET и при ошибках передаём контекст (messages автоматически попадает в контекст)
    return render(request, 'contacts.html')