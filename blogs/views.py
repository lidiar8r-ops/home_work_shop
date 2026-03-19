from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog


class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6  # Исправлено: 3 элементов на страницу

    def get_queryset(self):
        # Добавляем сортировку (например, по названию)
        return Blog.objects.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        # # Получаем последние 5 продуктов (по дате создания, от новых к старым)
        # latest_blogs = Blog.objects.order_by('-created_at')[:5]
        # # context['latest_blogs'] = latest_blogs

        return context


class BlogsDetailView(DetailView):
    model = Blog


class BlogsCreateView(CreateView):
    model = Blog
    template_name = 'blogs/blog_create.html'
    fields = ['title',
              'description',
              'image',
              'publication',
              'counter_views']
    success_url = reverse_lazy("blogs:blog_list")


class BlogsUpdateView(UpdateView):
    model = Blog
    template_name = 'blogs/blog_create.html'
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("blogs:blog_list")


class BlogsDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blogs_list")
