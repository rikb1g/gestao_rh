from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit,HorasExtraCreate,HorasExtraDelete


urlpatterns = [
    path('', HoraExtraList.as_view(),name='list_hora_extra'),
    path('atualizar/<int:pk>',HoraExtraEdit.as_view(),name='update_hora_extra'),
    path('eliminar/<int:pk>',HorasExtraDelete.as_view(),name='delete_hora_extra'),
    path('nova/', HorasExtraCreate.as_view(),name='new_hora')

]