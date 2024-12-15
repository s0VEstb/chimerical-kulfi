from django import forms
from .models import Cart, CartItem
from apps.main_page.models import Product
from django.contrib import admin


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CartItemInline(admin.TabularInline): 
    model = CartItem
    form = CartItemForm
    extra = 1  


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    inlines = [CartItemInline]  
