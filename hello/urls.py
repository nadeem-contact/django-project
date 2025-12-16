from django.urls import path
from .views import (
    ItemListCreateAPIView, ItemDetailAPIView,
    ProductListCreateAPIView, ProductDetailAPIView, 
    CustomerListCreateAPIView, CustomerDetailAPIView
)

urlpatterns = [
    # Item APIs
    path('items/', ItemListCreateAPIView.as_view()),
    path('items/<int:pk>/', ItemDetailAPIView.as_view()),

    # Product APIs
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),

    path('customer/', CustomerListCreateAPIView.as_view()),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view()),
]