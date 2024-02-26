from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Funcionario

def home(request):
    return HttpResponse("Olá")


class FuncionarioList(ListView):
    model = Funcionario