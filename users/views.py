from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pages:home')
        else:
            return redirect('users:registration')
    form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'registration/registration.html', context=context)

def signout(request):
    logout(request)
    return redirect('users:registration')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pages:home')
        else:
            form = UserCreationForm()
            context = {
                "form": form
            }
            return render(request, 'registration/registration.html', context=context)
    else:
        form = UserCreationForm()
        return render(request, 'registration/registration.html')