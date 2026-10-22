"""
URL configuration for projeto4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from filmes.views import inicio
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from filmes.views import FilmesViewSet, GenerosViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'generos', GenerosViewSet)  # registra endpoints para generos
router.register(r'filmes', FilmesViewSet)    # registra endpoints para filmes[cite: 5]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),          # adicione a rota para a sua API[cite: 5]
    path('api-token-auth/', obtain_auth_token), # adicione a rota para obter token via cli[cite: 5]
    path('', inicio, name='inicio'),
]