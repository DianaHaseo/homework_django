from django.urls import path

from catalog.views import (
    ContactView,
    ProductCreateView,
    ProductDetailView,
    ProductListView,
)


urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
        name="home",
    ),
    path(
        "contacts/",
        ContactView.as_view(),
        name="contacts",
    ),
    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product_create",
    ),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
]