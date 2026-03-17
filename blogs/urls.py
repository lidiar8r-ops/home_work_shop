from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogDetailView, ContactView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    # # path("", home, name="home"),
    # path("", BlogListView.as_view(), name='Blogs_list'),
    # path("catalog/<int:pk>/", BlogDetailView.as_view(), name='Blogs_detail'),
    # path("contacts/", ContactView.as_view(), name="contacts"),
    # path("catalog/create/", BlogCreateView.as_view(), name="Blogs_create"),
    # path("catalog/<int:pk>/update/", BlogUpdateView.as_view(), name="Blogs_update"),
    # path("catalog/<int:pk>/delete/", BlogDeleteView.as_view(), name="Blogs_delete"),
]
