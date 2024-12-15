from django.shortcuts import render
from .models import Banner, Category, Product, Footer
from .serilazers import BannerSerializer, CategorySerializer, ProductSerializer, FooterSerializer
from rest_framework import generics


class BannerListAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.select_related('category')


class FooterListAPIView(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
