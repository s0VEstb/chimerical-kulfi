from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart


class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем корзину текущего пользователя, создаем если её нет
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart.items.all()  # Возвращаем все элементы корзины

    def perform_create(self, serializer):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        product_id = self.request.data.get('product')
        if not product_id:
            raise ValidationError({'product': 'This field is required.'})
        print(self.request.data)
        
        # Проверяем наличие товара
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")
        
        # Проверяем, если товар уже есть в корзине
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        
        if cart_item:
            # Если товар есть, увеличиваем количество
            cart_item.quantity += 1
            cart_item.save()
        else:
            # Если товара нет в корзине, создаем новый элемент
            serializer.save(cart=cart, product=product)
