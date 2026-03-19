from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'blogs/blog_list.html'
    context_object_name = 'products'
    paginate_by = 3  # Исправлено: 3 элементов на страницу

    def get_queryset(self):
        # Добавляем сортировку (например, по названию)
        return Product.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем последние 5 продуктов (по дате создания, от новых к старым)
        latest_products = Product.objects.order_by('-created_at')[:5]
        context['latest_products'] = latest_products

        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    template_name = 'blogs/blog_create.html'
    fields = ["name", "description", "image", "category", "price"]
    success_url  = reverse_lazy("blog:blog_list")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'blogs/blog_create.html'
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("blog:blog_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("blog:blog_list")


class ContactView(TemplateView):
    model = Contact
    template_name = 'blogs/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем актуальные контактные данные (например, первый объект в БД)
        context['contact_info'] = Contact.objects.first()  # или filter().first()
        return context
