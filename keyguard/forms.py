from django import forms
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = '__all__'

class AutorizacaoForm(forms.ModelForm):
    class Meta:
        model = Autorizacao
        fields = '__all__'

class PosseForm(forms.ModelForm):
    class Meta:
        model = Posse
        fields = '__all__'

class StatusGeralForm(forms.ModelForm):
    class Meta:
        model = StatusGeral
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento', 'senha']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
