from django.forms import ModelForm
from .models import RegistoHoraExtra
from apps.funcionarios.models import Funcionario

class RegistoHoraExtraFrom(ModelForm):
    def __init__(self,user, *args, **kwargs):
        super(RegistoHoraExtraFrom, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)

    class Meta:
        model = RegistoHoraExtra
        fields = ['motivo', 'funcionario', 'horas']