from django.contrib import admin
from . models import CategoryModel, FoodModel, Cart, CartItem
# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title'
    ]


@admin.register(FoodModel)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'category', 'created_at', 'updated_at'
    ]
    list_filter = [
        'category', 'is_new'
    ]
    search_fields = [
        'title'
    ]


class CartProductInline(admin.TabularInline):
    model = CartItem
    extra = 0
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'status', 'created_at', 'updated_at'
    ]
    list_filter = [
        'status'
    ]
    inlines = [
        CartProductInline
    ]

@admin.register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = [
        'product'
    ]