from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from . models import FoodModel, CategoryModel, Cart, CartItem
from . forms import FoodForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

class FoodListView(ListView):
    model = FoodModel
    template_name = 'menu.html'
    context_object_name = 'food'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['new'] = FoodModel.objects.filter(is_new=True)
        context['food'] = FoodModel.objects.all()
        context['category'] = CategoryModel.objects.all()
        return context


class FoodDetailView(DetailView):
    template_name = 'food_detail.html'
    context_object_name = 'food'
    model = FoodModel


#Chopping Cart
def shoppingcart(request):
    context = {}
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if Cart.objects.exclude(status='order').exclude(status='not_active').filter(user=user).exists():
            context = {
                'cart': Cart.objects.exclude(status='order').exclude(status='not_active').get(user=user).id
            }
            return render(request, 'cart_error.html', context=context)
        cart = Cart.objects.filter(user=user, status='order').first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            context = {'cart_items': cart_items}
            context['cart'] = Cart.objects.filter(user=user).filter(status='order').first()
        return render(request, template_name='cart.html', context=context)
    else:
        return HttpResponse('войдите в аккаунт')


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if Cart.objects.exclude(status='order').exclude(status='not_active').filter(user=user).exists():
            context = {
                'cart': Cart.objects.exclude(status='order').exclude(status='not_active').get(user=user).id
            }
            return render(request, 'cart_error.html', context=context)
        cart, created = Cart.objects.get_or_create(user=user, status='order')
        product = FoodModel.objects.get(id=product_id)
        cart_product, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        cart_product.quantity += 1
        cart_product.save()
        return redirect(reverse_lazy('products:menu'))
    else:
        return HttpResponse('войдите в аккаунт')
    


def minus_quattity(request, product_id):
    user = request.user
    product = FoodModel.objects.get(id=product_id)
    cart = get_object_or_404(Cart, user=user, status='order')
    cart_product = get_object_or_404(CartItem, cart=cart, product=product)
    cart_product.quantity -= 1
    cart_product.save()
    if cart_product.quantity <= 0:
        cart_product.delete()
    return redirect(reverse_lazy('products:cart'))


def plus_quattity(request, product_id):
    user = request.user
    cartitem = get_object_or_404(
        CartItem, cart__user=user, product__id=product_id, cart__status='order')
    cartitem.quantity += 1
    cartitem.save()
    return redirect(reverse_lazy('products:cart'))


def cartitem_delete(request, product_id):
    user = request.user
    cartitem = get_object_or_404(
        CartItem, cart__user=user, product__id=product_id, cart__status='order')
    cartitem.delete()
    return redirect(reverse_lazy('products:cart'))


def update_cart(request, cart_id):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        cart = Cart.objects.get(id=cart_id)
        cart.phone = phone
        cart.address = address
        cart.status = 'processing'
        cart.total_price = cart.get_total_price()
        cart.save(update_fields=['phone', 'address', 'status', 'total_price'])
        return redirect(reverse('products:order', kwargs={'cart_id': cart_id}))

def cart_delete(request, cart_id):
    cart = Cart.objects.exclude(status='order').exclude(
        status='delivered').get(id=cart_id)
    cart.delete()
    return redirect('products:menu')

#Orders
def order(request, cart_id):
    cartitem = CartItem.objects.filter(cart__id=cart_id)
    order = Cart.objects.get(id=cart_id)
    STATUS_CHOICES = Cart._meta.get_field('status').choices
    context = {
        'order': order,
        'STATUS_CHOICES': STATUS_CHOICES,
        'cart_items': cartitem
    }
    return render(request, template_name='order.html', context=context)


def order_finish(request, cart_id):
    if request.method == 'POST':
        review = request.POST.get('review')
        cart = Cart.objects.get(id=cart_id)
        cart.review = review
        cart.status = 'not_active'
        cart.save(update_fields=('review', 'status'))
        return redirect('pages:home')
    
def user_orders_list(request):
    user = request.user
    not_active_order = Cart.objects.filter(status='not_active').order_by('-id')
    active_order = Cart.objects.exclude(status='order').exclude(
        status='not_active').filter(user=user)
    STATUS_CHOICES = Cart._meta.get_field('status').choices
    context = {
        'not_active_order': not_active_order,
        'active_order': active_order,
        'STATUS_CHOICES': STATUS_CHOICES
    }
    return render(request, 'user_orders.html', context=context)