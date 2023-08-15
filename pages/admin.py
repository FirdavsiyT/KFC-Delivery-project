from django.contrib import admin
from . models import BannerModel
# Register your models here.
@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'food', 'created_at', 'updated_at'
    ]