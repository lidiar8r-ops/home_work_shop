from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    path("", ProductListView.as_view(), name='products_list'),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/edit/", ProductUpdateView.as_view(), name="products_form"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_form"),
]
