from django.urls import path

from blogs.apps import BlogsConfig
# from blogs.views import BlogsListView, BlogsDetailView, ContactView, BlogsCreateView, BlogsUpdateView, \
#     BlogsDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    # # path("", home, name="home"),
    # path("", BlogsListView.as_view(), name='Blogs_list'),
    # path("catalog/<int:pk>/", BlogsDetailView.as_view(), name='Blogs_detail'),
    # path("contacts/", ContactView.as_view(), name="contacts"),
    # path("catalog/create/", BlogsCreateView.as_view(), name="Blogs_create"),
    # path("catalog/<int:pk>/update/", BlogsUpdateView.as_view(), name="Blogs_update"),
    # path("catalog/<int:pk>/delete/", BlogsDeleteView.as_view(), name="Blogs_delete"),
]
