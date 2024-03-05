from django.shortcuts import render
from django.urls import reverse_lazy
from .models import RegistoHoraExtra
from .forms import RegistoHoraExtraFrom

from django.views.generic import ListView, UpdateView, DeleteView, CreateView


class HoraExtraList(ListView):
    model = RegistoHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistoHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistoHoraExtra
    fields = ['motivo','funcionario','horas']


class HorasExtraDelete(DeleteView):
    model = RegistoHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HorasExtraCreate(CreateView):
    model = RegistoHoraExtra
    form_class = RegistoHoraExtraFrom

    def get_form_kwargs(self):
        kwargs = super(HorasExtraCreate,self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs


