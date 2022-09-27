from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

# Create your views here.


# LOGIN VIEW
def loginPage(request):
    form = UserLoginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Nie znaleziono użytkownika')
            print('nie znaleziono uzytkownika')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('products')
        else:
            messages.error(request, 'Nie zostało podane poprawne hasło. Spróbuj ponownie!')

    context = {"form": form}
    return render(request, 'users/login.html', context)



# REGISTER VIEW
def registerPage(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'Konto zostało utworzone! Udanych zakupów!')
            login(request, user)
            return redirect('products')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')