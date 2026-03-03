from django.views.generic import DetailView, ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 6  # Исправлено: 6 элементов на страницу

    def get_queryset(self):
        # Добавляем сортировку (например, по названию)
        return Product.objects.order_by('name')

class ProductDetailView(DetailView):
    model = Product

# def home(request):
#     # Выбираем последние 5 созданных продуктов (по полю created_at)
#     latest_products = Product.objects.order_by('-created_at')[:5]
#
#     # Выводим в консоль (для отладки)
#     for product in latest_products:
#         print(f"Продукт: {product.name}, Цена: {product.price}, Дата: {product.created_at}")
#
#     context = {
#         'latest_products': latest_products
#     }
#     return render(request, 'home.html', context)
#
#
# def contacts(request):
#     """
#     Обработка GET и POST запросов для страницы контактов.
#     При успешной отправке формы — перенаправление на ту же страницу с сообщением.
#     """
#
#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         if name and phone and message:
#             # Здесь можно добавить логику сохранения/отправки
#             messages.success(request, 'Сообщение отправлено!')
#             return redirect('catalog:contacts')
#         else:
#             messages.error(request, 'Заполните все поля!')
#     else:
#         contact_info = Contact.objects.first()  # Получаем первую запись
#         return render(request, 'contacts.html', {'contact_info': contact_info})
#     # Для GET и при ошибках передаём контекст (messages автоматически попадает в контекст)
#     return render(request, 'contacts.html')
#
#
# def products_list(request):
#     products = Product.objects.all()
#     paginator = Paginator(products, 6)  # 6 элементов на странице
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         "products": page_obj,  # Теперь передаем сам объект пагинации
#         "is_paginated": paginator.num_pages > 1
#     }
#     return render(request, 'product_list.html', context)
#
#
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)


