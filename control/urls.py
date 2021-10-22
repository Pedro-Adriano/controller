from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from registration.views import login_user, submit_login, user_register, register_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_user),
    path("login/submit", submit_login),
    path("login/register/", register_user),
    path("login/register/submit", user_register),
]
