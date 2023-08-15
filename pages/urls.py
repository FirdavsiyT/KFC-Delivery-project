from django.urls import path
from . views import IndexListView
app_name = 'pages'

urlpatterns = [
    path('', IndexListView.as_view(), name='home')
]