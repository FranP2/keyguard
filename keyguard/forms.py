

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario, Chave, Autorizacao, Posse, Sala, StatusGeral

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'senha', 'telefone']

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['numero', 'descricao']

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = ['identificador', 'sala']

class AutorizacaoForm(forms.ModelForm):
    class Meta:
        model = Autorizacao
        fields = ['usuario', 'chave']

class PosseForm(forms.ModelForm):
    class Meta:
        model = Posse
        fields = ['usuario', 'chave', 'data_devolucao']

class StatusGeralForm(forms.ModelForm):
    class Meta:
        model = StatusGeral
        fields = ['chave', 'disponivel']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
