from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Rota direta para o template base
    # Rotas para Usuários
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuarios/novo/', views.novo_usuario, name='novo_usuario'),
    path('usuarios/<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/deletar/', views.deletar_usuario, name='deletar_usuario'),

    # Rotas para Salas
    path('salas/', views.lista_salas, name='lista_salas'),
    path('salas/<int:pk>/', views.detalhes_sala, name='detalhes_sala'),
    path('salas/nova/', views.nova_sala, name='nova_sala'),
    path('salas/<int:pk>/editar/', views.editar_sala, name='editar_sala'),
    path('salas/<int:pk>/deletar/', views.deletar_sala, name='deletar_sala'),

    # Rotas para Chaves
    path('chaves/', views.lista_chaves, name='lista_chaves'),
    path('chaves/<int:pk>/', views.detalhes_chave, name='detalhes_chave'),
    path('chaves/nova/', views.nova_chave, name='nova_chave'),
    path('chaves/<int:pk>/editar/', views.editar_chave, name='editar_chave'),
    path('chaves/<int:pk>/deletar/', views.deletar_chave, name='deletar_chave'),

    # Rotas para Autorizações
    path('autorizacoes/', views.lista_autorizacoes, name='lista_autorizacoes'),
    path('autorizacoes/<int:pk>/', views.detalhes_autorizacao, name='detalhes_autorizacao'),
    path('autorizacoes/nova/', views.nova_autorizacao, name='nova_autorizacao'),
    path('autorizacoes/<int:pk>/editar/', views.editar_autorizacao, name='editar_autorizacao'),
    path('autorizacoes/<int:pk>/deletar/', views.deletar_autorizacao, name='deletar_autorizacao'),

    # Rotas para Posses
    path('posses/', views.lista_posses, name='lista_posses'),
    path('posses/<int:pk>/', views.detalhes_posse, name='detalhes_posse'),
    path('posses/nova/', views.nova_posse, name='nova_posse'),
    path('posses/<int:pk>/editar/', views.editar_posse, name='editar_posse'),
    path('posses/<int:pk>/deletar/', views.deletar_posse, name='deletar_posse'),

    # Rotas para Status Geral
    path('status/', views.lista_status_geral, name='lista_status_geral'),
    path('status/<int:pk>/', views.detalhes_status_geral, name='detalhes_status_geral'),
    path('status/novo/', views.novo_status_geral, name='novo_status_geral'),
    path('status/<int:pk>/editar/', views.editar_status_geral, name='editar_status_geral'),
    path('status/<int:pk>/deletar/', views.deletar_status_geral, name='deletar_status_geral'),
    path('nova_solicitacao/', views.nova_solicitacao, name='nova_solicitacao'),

    # Rotas de Registro e Login
    #path('registro/', views.registro_usuario, name='registro_usuario'),
    #path('login/', views.login_usuario, name='login_usuario'),
    #path('logout/', views.logout_usuario, name='logout_usuario'),
    


    # Configura a rota principal diretamente para a tela de login

    path('login/', views.login_usuario, name='login_usuario'),  # Tela inicial - Login
    path('registro/', views.registro_usuario, name='registro_usuario'),  # Tela de Registro
    path('logout/', views.logout_usuario, name='logout_usuario'),  # Logout
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),  # Página protegida (exemplo)
    
]






