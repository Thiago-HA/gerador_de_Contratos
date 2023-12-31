"""
URL configuration for geradorContratos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('abrir_contrato/<int:id>', views.contrato, name='contrato'),
    path('editar_contrato/<int:id>', views.editar_contrato, name='editar_contrato'),
    path('deletar_contrato/<int:id>', views.deletar_contrato, name='deletar_contrato'),
    path('cadastro_contrato', views.cadastro_contrato, name='cadastro_contrato'),
]
