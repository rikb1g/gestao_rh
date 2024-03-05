from django.urls import path
from .views import DepartamentoList, DepartamentoUpdate, DepartamentoCreate,DepartamentoDelete

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamento'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('atualizar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('eliminar/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
]
