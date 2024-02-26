from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario


def home(request):
    return HttpResponse("ola")


class FuncionariosList(ListView):
    model = Funcionario