

from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuario/novo/', views.novo_usuario, name='novo_usuario'),
    path('usuario/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuario/<int:pk>/deletar/', views.deletar_usuario, name='deletar_usuario'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
]
