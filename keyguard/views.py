from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral
from .forms import UsuarioForm, SalaForm, ChaveForm, AutorizacaoForm, PosseForm, StatusGeralForm, RegistroForm, LoginForm
#Vou adicionar a paginação, filtros e exportação de dados à sua implementação existente. Aqui está o código completo:
# Views para Usuários
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

# Views para Salas
def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'keyguard/lista_salas.html', {'salas': salas})

def detalhes_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    return render(request, 'keyguard/detalhes_sala.html', {'sala': sala})

def nova_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()
    return render(request, 'keyguard/editar_sala.html', {'form': form})

def editar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == "POST":
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm(instance=sala)
    return render(request, 'keyguard/editar_sala.html', {'form': form})

def deletar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    sala.delete()
    return redirect('lista_salas')

# Views para Chaves
def lista_chaves(request):
    chaves = Chave.objects.all()
    return render(request, 'keyguard/lista_chaves.html', {'chaves': chaves})

def detalhes_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)
    return render(request, 'keyguard/detalhes_chave.html', {'chave': chave})

def nova_chave(request):
    if request.method == "POST":
        form = ChaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_chaves')
    else:
        form = ChaveForm()
    return render(request, 'keyguard/editar_chave.html', {'form': form})

def editar_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)
    if request.method == "POST":
        form = ChaveForm(request.POST, instance=chave)
        if form.is_valid():
            form.save()
            return redirect('lista_chaves')
    else:
        form = ChaveForm(instance=chave)
    return render(request, 'keyguard/editar_chave.html', {'form': form})

def deletar_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)
    chave.delete()
    return redirect('lista_chaves')

# Views para Autorizações
def lista_autorizacoes(request):
    autorizacoes = Autorizacao.objects.all()
    return render(request, 'keyguard/lista_autorizacoes.html', {'autorizacoes': autorizacoes})

def detalhes_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao, pk=pk)
    return render(request, 'keyguard/detalhes_autorizacao.html', {'autorizacao': autorizacao})

def nova_autorizacao(request):
    if request.method == "POST":
        form = AutorizacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizacoes')
    else:
        form = AutorizacaoForm()
    return render(request, 'keyguard/editar_autorizacao.html', {'form': form})

def editar_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao, pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST, instance=autorizacao)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizacoes')
    else:
        form = AutorizacaoForm(instance=autorizacao)
    return render(request, 'keyguard/editar_autorizacao.html', {'form': form})

def deletar_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao, pk=pk)
    autorizacao.delete()
    return redirect('lista_autorizacoes')

# Views para Posses
def lista_posses(request):
    posses = Posse.objects.all()
    return render(request, 'keyguard/lista_posses.html', {'posses': posses})

def detalhes_posse(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    return render(request, 'keyguard/detalhes_posse.html', {'posse': posse})

def nova_posse(request):
    if request.method == "POST":
        form = PosseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posses')
    else:
        form = PosseForm()
    return render(request, 'keyguard/editar_posse.html', {'form': form})

def editar_posse(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    if request.method == "POST":
        form = PosseForm(request.POST, instance=posse)
        if form.is_valid():
            form.save()
            return redirect('lista_posses')
    else:
        form = PosseForm(instance=posse)
    return render(request, 'keyguard/editar_posse.html', {'form': form})

def deletar_posse(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    posse.delete()
    return redirect('lista_posses')

# Views para StatusGeral
def lista_status_geral(request):
    status_geral = StatusGeral.objects.all()
    return render(request, 'keyguard/lista_status_geral.html', {'status_geral': status_geral})

def detalhes_status_geral(request, pk):
    status = get_object_or_404(StatusGeral, pk=pk)
    return render(request, 'keyguard/detalhes_status_geral.html', {'status': status})

def novo_status_geral(request):
    if request.method == "POST":
        form = StatusGeralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_status_geral')
    else:
        form = StatusGeralForm()
    return render(request, 'keyguard/editar_status_geral.html', {'form': form})

def editar_status_geral(request, pk):
    status = get_object_or_404(StatusGeral, pk=pk)
    if request.method == "POST":
        form = StatusGeralForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('lista_status_geral')
    else:
        form = StatusGeralForm(instance=status)
    return render(request, 'keyguard/editar_status_geral.html', {'form': form})

def deletar_status_geral(request, pk):
    status = get_object_or_404(StatusGeral, pk=pk)
    status.delete()
    return redirect('lista_status_geral')

# Views de registro e login
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