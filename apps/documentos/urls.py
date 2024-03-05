from django.urls import path
from .views import DocumentCreate


urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentCreate.as_view(), name='create_document'),

]