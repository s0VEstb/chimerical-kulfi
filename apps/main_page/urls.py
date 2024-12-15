from django.urls import path
from .views import (BannerListAPIView, CategoryListAPIView, ProductListAPIView,
                     ProductDetailAPIView, CategoryDetailAPIView, FooterListAPIView)


urlpatterns = [
    path('banners/', BannerListAPIView.as_view(), name='banner_list'),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('footer/', FooterListAPIView.as_view(), name="footer")
]
