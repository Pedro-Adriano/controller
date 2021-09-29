from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_user(request):
    print("aquiu1")
    return render(request, "login.html")


@csrf_protect
def submit_login(request):
    print("aqui")
    if request.POST:
        print("aqui")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/login/#")
        else:
            messages.error(request, "Usuário e senha inválido. Favor tentar novamente")
    return redirect("/login/")
