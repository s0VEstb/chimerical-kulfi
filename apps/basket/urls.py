from django.urls import path
from .views import CartView, CartItemListCreateView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-items'),
]