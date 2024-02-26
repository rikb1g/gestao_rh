from django.db import models
from Apps.funcionarios.models import Funcionario
class RegistoHoraExta(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
