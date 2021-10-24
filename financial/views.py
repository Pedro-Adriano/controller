from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login


def bill_to_pay(request):
    return render(request, "bills_to_pay.html")
