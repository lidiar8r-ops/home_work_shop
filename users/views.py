from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from users.models import User


# Create your views here.
class UserCreateView(View):
    model = User
    form_class = UserCreationForm
    sucess_url = reverse_lazy('users:login')

