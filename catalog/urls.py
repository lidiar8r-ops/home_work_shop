from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("", ProductListView.as_view(), name='products_list'),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
]
