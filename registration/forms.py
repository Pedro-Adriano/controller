from django.forms import ModelForm
from registration.models import UserModel


class UserForm(ModelForm):
    class Meta:
        models = UserModel
        fields = ["cpf", "password", "email"]
