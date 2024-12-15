from .models import Banner, Category, Product, Footer
from rest_framework import serializers


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'image', 'title', 'description', 'description_litle', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'products')

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)
        return ProductSerializer(products, many=True).data



class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'image', 'price', 'category_name', 'created_at', 'updated_at')

    def get_category_name(self, obj):
        return obj.category.name



class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('id', 'title', 'link', 'instagram', 'telegram', 'whatsapp', 'logo')