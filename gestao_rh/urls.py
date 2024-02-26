from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('Apps.core.urls')),
    path('funcionarios/', include('Apps.funcionarios.urls')),
    path('empresa/', include('Apps.empresa.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
