from django.urls import path
from .views import ProductListCreateAPIView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
