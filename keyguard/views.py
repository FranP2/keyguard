from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral
from .forms import UsuarioForm, SalaForm, ChaveForm, AutorizacaoForm, PosseForm, StatusGeralForm, RegistroForm, LoginForm

def home(request):
    # Renderiza o template base diretamente sem qualquer herança
    return render(request, 'home.html')
# Views para Usuário
def lista_usuarios(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    usuarios = Usuario.objects.filter(nome__icontains=query) if query else Usuario.objects.all()
    paginator = Paginator(usuarios, 10)  # Paginação
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request, 'keyguard/lista_usuarios.html', {'usuarios': usuarios, 'query': query})

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


# ============================
# Views para Salas
# ============================
def lista_salas(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    salas = Sala.objects.filter(nome__icontains=query) if query else Sala.objects.all()
    paginator = Paginator(salas, 10)  # Paginação
    page = request.GET.get('page')
    salas = paginator.get_page(page)
    return render(request, 'keyguard/listasalas.html', {'salas': salas, 'query': query})

def detalhes_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    return render(request, 'keyguard/listasala.html', {'sala': sala})

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


# ============================
# Views para Chaves
# ============================
def lista_chaves(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    chaves = Chave.objects.filter(codigo__icontains=query) if query else Chave.objects.all()
    paginator = Paginator(chaves, 10)  # Paginação
    page = request.GET.get('page')
    chaves = paginator.get_page(page)
    return render(request, 'keyguard/lista_chaves.html', {'chaves': chaves, 'query': query})

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


# ============================
# Views para Autorizações
# ============================
def lista_autorizacoes(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    autorizacoes = Autorizacao.objects.filter(nome__icontains=query) if query else Autorizacao.objects.all()
    paginator = Paginator(autorizacoes, 10)
    page = request.GET.get('page')
    autorizacoes = paginator.get_page(page)
    return render(request, 'keyguard/lista_autorizacoes.html', {'autorizacoes': autorizacoes, 'query': query})

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


# ============================
# Views para Posses
# ============================
def lista_posses(request):
    query = request.GET.get('q', '')
    posses = Posse.objects.filter(usuario__nome__icontains=query) if query else Posse.objects.all()
    paginator = Paginator(posses, 10)
    page = request.GET.get('page')
    posses = paginator.get_page(page)
    return render(request, 'keyguard/lista_posses.html', {'posses': posses, 'query': query})

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


# ============================
# Views para Status Geral
# ============================
def lista_status_geral(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    status_geral = StatusGeral.objects.filter(autorizacao__nome__icontains=query) if query else StatusGeral.objects.all()
    paginator = Paginator(status_geral, 10)  # Paginação com 10 itens por página
    page = request.GET.get('page')
    status_geral = paginator.get_page(page)
    return render(request, 'keyguard/lista_status_geral.html', {'status_geral': status_geral, 'query': query})

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


# ============================
# Views de Registro e Login
# ============================
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # Formulário de autenticação padrão do Django
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Loga o usuário
            return redirect('/home/')  # Redireciona para a tela de home
        else:
            messages.error(request, "Usuário ou senha inválidos.")  # Mensagem de erro
    else:
        form = AuthenticationForm()
    return render(request, 'front_end/login.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import UsuarioForm

from django.shortcuts import render, redirect
from .forms import UsuarioForm  # Certifique-se de que o formulário para registro existe

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o usuário no banco de dados
            return redirect('login_usuario')  # Redireciona para a página de login ou outro local
    else:
        form = UsuarioForm()

    return render(request, 'front_end/cadastro.html', {'form': form})


def logout_usuario(request):
    logout(request)  # Faz logout
    messages.success(request, "Você saiu com sucesso.")
    return redirect('login_usuario')  # Redireciona para a tela de login

from django.shortcuts import render, redirect
from .forms import SolicitacaoPosseChaveForm
from .models import SolicitacaoPosseChave

def nova_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoPosseChaveForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a solicitação no banco de dados
            return redirect('lista_posses')  # Redireciona para a lista de posses
    else:
        form = SolicitacaoPosseChaveForm()  # Exibe o formulário vazio

    return render(request, 'keyguard/nova_solicitacao.html', {'form': form})
