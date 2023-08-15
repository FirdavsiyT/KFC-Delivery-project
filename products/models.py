from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class FoodModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    image = models.ImageField(upload_to='products')
    price = models.FloatField(verbose_name=_('price'))
    ru_description = models.TextField(verbose_name=_('ru_description'),null=True, blank=True)
    uz_description = models.TextField(verbose_name=_('uz_description'), null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    is_new = models.BooleanField(verbose_name=_('is new'), default=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    def new_count(self):
        counter = 0
        for i in self.is_new:
            if i is True:
                counter += 1
        return counter

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Food')


class Cart(models.Model):
    STATUS_CHOICES = (
        ('order', 'Заказ'),
        ('processing', 'Обработка'),
        ('cooking', 'Готовится'),
        ('shipped', 'В пути'),
        ('delivered', 'Доставлен'),
        ('not_active', 'Не активен')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='order')
    phone = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=128, blank=True)
    review = models.TextField(blank=True)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self) -> str:
        return f"{self.user.username}'s Cart"
    
    def get_total_price(self):
        total = 0
        for item in self.cart.all():
            total += item.product.price * item.quantity
        return total

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')