from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral, SolicitacaoPosseChave
from .forms import UsuarioForm, SalaForm, ChaveForm, AutorizacaoForm, PosseForm, StatusGeralForm, RegistroForm, LoginForm, SolicitacaoPosseChaveForm,UserCreationForm,AuthenticationForm,ClienteForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
import json

def home(request):
    # Renderiza o template base diretamente sem qualquer herança
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'Inicial_App.html')  # Certifique-se de que o arquivo está na pasta 'templates'

# Views para Usuário
def lista_usuarios(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    # Filtra apenas os clientes (is_staff=False)
    usuarios = Usuario.objects.filter(is_staff=False, nome__icontains=query) if query else Usuario.objects.filter(is_staff=False)
    paginator = Paginator(usuarios, 10)  # Paginação
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request, 'listausuario.html', {'usuarios': usuarios, 'query': query})

def detalhes_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalhes_usuario.html', {'usuario': usuario})

def novo_usuario(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # Evita salvamento automático
            # Marca o usuário como cliente
            usuario.is_staff = False
            usuario.is_superuser = False
            usuario.save()  # Agora salva no banco
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('lista_usuarios')  # Redireciona para a lista de usuários
    else:
        form = UsuarioForm()

    return render(request, 'UsuárioCadastrado.html', {'form': form})

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



@csrf_exempt
def deletar_usuario(request, pk):
    if request.method == 'DELETE':
        try:
            usuario = Usuario.objects.get(pk=pk)
            usuario.delete()
            return JsonResponse({'message': 'Usuário excluído com sucesso!'})
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado.'}, status=404)
    return JsonResponse({'error': 'Método não permitido.'}, status=405)


# Views para Salas

def lista_salas(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    salas = Sala.objects.filter(nome__icontains=query).order_by('-id') if query else Sala.objects.all().order_by('-id')  # Ordenação por ID decrescente
    paginator = Paginator(salas, 10000)  # Paginação
    page = request.GET.get('page')
    salas = paginator.get_page(page)
    return render(request, 'ListaSalas.html', {'salas': salas, 'query': query})

def detalhes_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    return render(request, 'keyguard/listasala.html', {'sala': sala})

def nova_sala(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')  # Redireciona para a página de lista de salas após o sucesso
    else:
        form = SalaForm()

    return render(request, 'sala.html', {'form': form})


@csrf_exempt
def editar_sala(request, pk):
    if request.method == 'PUT':
        sala = Sala.objects.get(pk=pk)
        data = json.loads(request.body)
        sala.nome = data.get('nome', sala.nome)
        sala.save()
        return JsonResponse({'status': 'success', 'message': 'Sala editada com sucesso!'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def deletar_sala(request, pk):
    if request.method == 'DELETE':
        sala = Sala.objects.get(pk=pk)
        sala.delete()
        return JsonResponse({'status': 'success', 'message': 'Sala apagada com sucesso!'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido.'}, status=405)



# Views para Chaves

def lista_chaves(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    # Ordenar pelo campo de criação, mais antigas no final
    chaves = Chave.objects.filter(codigo__icontains=query).order_by('id') if query else Chave.objects.all().order_by('id')
    paginator = Paginator(chaves, 10)  # Paginação
    page = request.GET.get('page')
    chaves = paginator.get_page(page)
    return render(request, 'listachaves.html', {'chaves': chaves, 'query': query})


def detalhes_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)
    return render(request, 'keyguard/detalhes_chave.html', {'chave': chave})

def nova_chave(request):
    if request.method == "POST":
        form = ChaveForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo cadastro no banco de dados
            return redirect('lista_chaves')  # Redireciona para a lista de chaves
    else:
        form = ChaveForm()

    return render(request, 'cadastrochaves.html', {'form': form})
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
    query = request.GET.get('q', '')  # Busca dinâmica
    autorizacoes = Autorizacao.objects.filter(nome__icontains=query) if query else Autorizacao.objects.all()
    autorizacoes = autorizacoes.order_by('-id')  # Ordenação para consistência
    paginator = Paginator(autorizacoes, 10000)
    page = request.GET.get('page')
    autorizacoes = paginator.get_page(page)
    return render(request, 'listaAutorizacao.html', {'autorizacoes': autorizacoes, 'query': query})

def detalhes_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao, pk=pk)
    return render(request, 'detalhes_autorizacao.html', {'autorizacao': autorizacao})

'''def nova_autorizacao(request):
    if request.method == "POST":
        form = AutorizacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizacoes')
    else:
        form = AutorizacaoForm()
    return render(request, 'cadastroautorizacao.html', {'form': form})'''


def nova_autorizacao(request):
    if request.method == "POST":
        form = AutorizacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizacoes')  # Redireciona para a lista
    else:
        form = AutorizacaoForm()
    
    salas = Sala.objects.all()  # Busca todas as salas cadastradas
    return render(request, 'cadastroautorizacao.html', {'form': form, 'salas': salas})

def editar_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao, pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST, instance=autorizacao)
        if form.is_valid():
            form.save()
            return redirect('lista_autorizacoes')
    else:
        form = AutorizacaoForm(instance=autorizacao)
    return render(request, 'editar_autorizacao.html', {'form': form})



def excluir_autorizacao(request, id):
    if request.method == 'POST':  # Aceitamos apenas requisições POST para exclusão
        try:
            autorizacao = Autorizacao.objects.get(id=id)
            autorizacao.delete()
            return JsonResponse({'status': 'success', 'message': 'Autorização excluída com sucesso!'})
        except Autorizacao.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Autorização não encontrada!'})
    return JsonResponse({'status': 'error', 'message': 'Requisição inválida!'})



def lista_posses(request):
    query = request.GET.get('q', '')
    posses = Posse.objects.filter(usuario__nome__icontains=query) if query else Posse.objects.all()
    paginator = Paginator(posses, 10)
    page = request.GET.get('page')
    posses = paginator.get_page(page)
    return render(request, 'possechaves.html', {'posses': posses, 'query': query})

@login_required
def nova_posse(request):
    message = ""
    if request.method == "POST":
        # Obtenha os valores dos campos enviados
        nome = request.POST.get('nome', '').strip()      # Se não for utilizado porque usamos request.user, apenas pode ser ignorado.
        chave_valor = request.POST.get('chave', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        motivo = request.POST.get('motivo', '').strip()
        
        # Verifica se todos os campos foram preenchidos
        if not (nome and chave_valor and telefone and motivo):
            message = "Todos os campos devem ser preenchidos."
            return render(request, 'cadastrposse.html', {'message': message})
        
        # Se "chave" for uma ForeignKey, obtenha a instância correspondente.
        try:
            # Supondo que no modelo Chave o campo que identifica seja 'codigo'
            chave_obj = Chave.objects.get(codigo=chave_valor)
        except Chave.DoesNotExist:
            message = "Chave não encontrada."
            return render(request, 'cadastrposse.html', {'message': message})
        
        # Crie o objeto Posse. O campo 'usuario' é atribuído como o usuário logado.
        try:
            posse = Posse(
                usuario=request.user,
                chave=chave_obj,
                telefone=telefone,
                motivo=motivo
            )
            posse.save()
            message = "Posse cadastrada com sucesso!"
        except Exception as e:
            message = f"Erro ao salvar: {str(e)}"
            return render(request, 'cadastrposse.html', {'message': message})
        
        # Ao salvar, em vez de redirecionar, re-renderizamos o formulário e exibimos a mensagem
        return render(request, 'cadastrposse.html', {'message': message})
    else:
        return render(request, 'cadastrposse.html')




def detalhes_posse(request, pk):
    posse = get_object_or_404(Posse, pk=pk)
    return render(request, 'keyguard/detalhes_posse.html', {'posse': posse})

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


def transferir_posse(request, posse_id):
    posse = get_object_or_404(Posse, id=posse_id)
    if request.method == 'POST':
        form = PosseForm(request.POST, instance=posse)
        if form.is_valid():
            form.save()
            return redirect('lista_posses')
    else:
        form = PosseForm(instance=posse)
    return render(request, 'transferir_posse.html', {'form': form})


# Views para Status Geral

def lista_status_geral(request):
    query = request.GET.get('q', '')  # Busca dinâmica
    status_geral = StatusGeral.objects.filter(autorizacao__nome__icontains=query) if query else StatusGeral.objects.all()
    paginator = Paginator(status_geral, 10)  # Paginação com 10 itens por página
    page = request.GET.get('page')
    status_geral = paginator.get_page(page)
    return render(request, 'statusgeral.html', {'status_geral': status_geral, 'query': query})

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

# Views de Registro e Login
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

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # Evita salvamento automático
            # Marca o usuário como administrador
            usuario.is_staff = True
            usuario.is_superuser = True
            usuario.save()  # Salva no banco
            return redirect('login_usuario')  # Redireciona para login ou outra página
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})

def logout_usuario(request):
    logout(request)  # Faz logout
    messages.success(request, "Você saiu com sucesso.")
    return redirect('login_usuario')  # Redireciona para a tela de login

def nova_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoPosseChaveForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a solicitação no banco de dados
            return redirect('lista_posses')  # Redireciona para a lista de posses
    else:
        form = SolicitacaoPosseChaveForm()  # Exibe o formulário vazio

    return render(request, 'keyguard/nova_solicitacao.html', {'form': form})

def solicitar_posse(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')  # Captura o nome enviado pelo formulário
        return render(request, 'solicitarPosse.html', {'nome': nome})

    # Renderiza a página padrão para GET
    return render(request, 'solicitarPosse.html')



def obter_lista(request):
    categoria = request.GET.get('categoria')
    
    if categoria == "Sala":
        dados = list(Sala.objects.values('id', 'nome', 'status'))
    elif categoria == "Chave":
        dados = list(Chave.objects.values('id', 'nome'))
    elif categoria == "Usuario":
        dados = list(Usuario.objects.values('id', 'nome'))
    elif categoria == "Posse":
        dados = list(Posse.objects.values('id', 'chave_id', 'usuario_id'))
    elif categoria == "Autorizacao":
        dados = list(Autorizacao.objects.values('id', 'usuario_id', 'sala_id', 'status'))
    else:
        dados = []
    
    return JsonResponse({'dados': dados})
