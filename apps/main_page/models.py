from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_litle = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.category.name}"
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Footer(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()
    whatsapp = models.URLField()
    logo = models.ImageField(upload_to='footer/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'