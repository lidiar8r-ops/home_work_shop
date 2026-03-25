from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(publication=True).order_by('-created_at')

class BlogsDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.counter_views += 1
        obj.save()
        return obj


class BlogsCreateView(CreateView):
    model = Blog
    template_name = 'blogs/blog_create.html'
    fields = ['title', 'description', 'image', 'publication']
    success_url = reverse_lazy("blogs:blog_list")


class BlogsUpdateView(UpdateView):
    model = Blog
    template_name = 'blogs/blog_create.html'  # Отдельный шаблон
    fields = ['title', 'description', 'image', 'publication']

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={'pk': self.object.pk})


class BlogsDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")