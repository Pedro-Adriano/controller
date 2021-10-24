from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import messages

from registration.models import UserModel
from registration.validate import ValidatorCPF


def login_user(request):
    return render(request, "login.html")


@csrf_protect
def submit_login(request):

    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = UserModel.objects.filter(cpf=username, password=password)

        if user:
            return redirect("/login/#")
        else:
            messages.error(request, "Usuário ou senha inválido. Favor tentar novamente")
    return redirect("/login/")


def register_user(request):
    return render(request, "register.html")


@csrf_exempt
def user_register(request):
    password = request.POST.get("password")
    username = request.POST.get("CPF")
    email = request.POST.get("E-mail")

    check_user = UserModel.objects.filter(cpf=username)
    validator = ValidatorCPF(username)
    cpf_is_valid = validator.check_cpf_is_valid()

    if not cpf_is_valid:
        messages.error(request, "CPF inválido. Favor adicione um CPF válido")

    elif check_user:
        messages.error(request, "CPF já em uso")

    elif password and username and email:
        form = UserModel(password=password, cpf=username, email=email)
        form.save()
        return redirect("/login/")

    else:
        messages.error(
            request, "Adicione as informações corretas. Favor tentar novamente"
        )

    return redirect("/login/register/")
