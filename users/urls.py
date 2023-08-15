from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', view=views.signin, name='registration'),
    path('signup', view=views.signup, name='signup'),
    path('signout/', view=views.signout, name='signout'),
]