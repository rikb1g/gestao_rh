from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa                     
    fields = ['nome']

    def form_valid(self, form):
        objeto = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = objeto
        funcionario.save()
        return HttpResponse('OK')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']

class CriarEmpresa(UpdateView):
    model = Empresa
    fields = ['nome']   
