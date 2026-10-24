from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, DeleteView, UpdateView, CreateView

from .forms import ProductForm, ProductModeratorForm
from .models import Product, Contact
from .services import get_category_by_key, get_product, get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 6  # Исправлено: 3 элементов на страницу

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
    template_name = "catalog/product_detail.html"

    def get_object(self, queryset=None):
        # Низкоуровневое кеширование страницы продукта: product_detail_{id}
        product = get_product(self.kwargs.get(self.pk_url_kwarg or "pk"))
        if product is None:
            raise Http404("Продукт не найден")
        return product


class CategoryProductsView(TemplateView):
    """Список продуктов категории. Принимает id или slug."""

    template_name = "catalog/category_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_category_by_key(self.kwargs["category_key"])
        if category is None:
            raise Http404("Категория не найдена")
        context["category"] = category
        context["products"] = get_products_by_category(category)
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')  # перенаправление на список товаров

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user == product.owner or request.user.has_perm('catalog.delete_product'):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


class ContactView(TemplateView):
    model = Contact
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем актуальные контактные данные (например, первый объект в БД)
        context['contact_info'] = Contact.objects.first()  # или filter().first()
        return context
