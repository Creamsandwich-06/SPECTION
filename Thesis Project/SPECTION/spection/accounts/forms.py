

from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from .models import Order

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(BSModalModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    phone = forms.CharField(label="Phone", max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
