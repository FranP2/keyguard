

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, Chave, Autorizacao, Posse, Sala, StatusGeral
from .forms import UsuarioForm, SalaForm, ChaveForm, AutorizacaoForm, PosseForm, StatusGeralForm, RegistroForm, LoginForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'keyguard/lista_usuarios.html', {'usuarios': usuarios})

def detalhes_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'keyguard/detalhes_usuario.html', {'usuario': usuario})

def novo_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'keyguard/editar_usuario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'keyguard/editar_usuario.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('lista_usuarios')
    else:
        form = RegistroForm()
    return render(request, 'keyguard/registro.html', {'form': form})

def login_usuario(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_usuarios')
    else:
        form = LoginForm()
    return render(request, 'keyguard/login.html', {'form': form})
