from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from products.models import FoodModel
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = FoodModel

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['new'] = FoodModel.objects.filter(is_new=True)
        context['burgers'] = FoodModel.objects.filter(category__title='Бургеры')
        return context