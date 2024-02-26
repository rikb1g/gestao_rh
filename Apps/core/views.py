from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.funcionarios.models import Funcionario


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    print(request.user)  # Verifica o conteúdo do usuário no console do servidor
    return render(request, 'core/index.html', data)

