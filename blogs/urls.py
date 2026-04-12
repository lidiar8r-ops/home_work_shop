from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogsListView, BlogsDetailView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView

# from blogs.views import BlogsListView, BlogsDetailView, ContactView, BlogsCreateView, BlogsUpdateView, \
#     BlogsDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    # # path("", home, name="home"),
    path("", BlogsListView.as_view(), name='blog_list'),
#     path('', BlogsListView.as_view(), name='blog_list'),  ]
    path("blogs/<int:pk>/", BlogsDetailView.as_view(), name='blog_detail'),
    path("blogs/create/", BlogsCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/update/", BlogsUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogsDeleteView.as_view(), name="blog_delete"),
]
