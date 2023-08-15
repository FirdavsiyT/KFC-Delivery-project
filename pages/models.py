from django.db import models
from django.utils.translation import gettext as _
from products.models import FoodModel

# Create your models here.

class BannerModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    image = models.ImageField(upload_to='products')
    description = models.TextField(verbose_name=_('description'))
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')