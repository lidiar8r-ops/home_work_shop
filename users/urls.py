from tempfile import template

from django.contrib.auth.views import LoginView
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login", LoginView.as_view(template_name="login.html"), ),
]
