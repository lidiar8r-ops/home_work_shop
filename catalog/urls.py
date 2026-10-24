from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    CategoryProductsView,
    ContactView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    path("", ProductListView.as_view(), name='products_list'),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
    path("category/<str:category_key>/", CategoryProductsView.as_view(), name="category_products"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
]
