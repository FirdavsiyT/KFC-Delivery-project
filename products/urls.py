from django.urls import path
from . import views
from . import views
from .views import FoodListView, FoodDetailView

app_name = 'products'

urlpatterns = [
    path('', FoodListView.as_view(), name='menu'),
    path('food/detail/<int:pk>/', FoodDetailView.as_view(), name='detail'),
    path('shopping/cart/', view=views.shoppingcart, name='cart'),
    path('add/cartitem/cart/<int:product_id>', view=views.add_to_cart, name='add_to_cart'),
    path('minus/cartitem/cart/<int:product_id>', view=views.minus_quattity, name='minus_cartitem'),
    path('plus/cartitem/cart/<int:product_id>', view=views.plus_quattity, name='plus_cartitem'),
    path('delete/cartitem/cart/<int:product_id>', view=views.cartitem_delete, name='delcartitem'),
    path('update/cart/<int:cart_id>', view=views.update_cart, name='update_cart'),
    path('order/finish/<int:cart_id>', view=views.order_finish, name='order_finish'),
    path('order/<int:cart_id>/', view=views.order, name='order'),
    path('cart/delete<int:cart_id>', view=views.cart_delete, name='cart_delete'),
    path('user/orders/', view=views.user_orders_list, name='orders_list')
]