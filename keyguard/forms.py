from django import forms
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral

# Formulário para o modelo Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento', 'is_staff', 'is_superuser']

# Formulário para o modelo Sala
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

# Formulário para o modelo Chave
class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = '__all__'

# Formulário para o modelo Autorizacao
class AutorizacaoForm(forms.ModelForm):
    class Meta:
        model = Autorizacao
        fields = '__all__'

# Formulário para o modelo Posse
class PosseForm(forms.ModelForm):
    class Meta:
        model = Posse
        fields = '__all__'

# Formulário para o modelo StatusGeral
class StatusGeralForm(forms.ModelForm):
    class Meta:
        model = StatusGeral
        fields = '__all__'

# Formulário de Registro de Usuário
class RegistroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirme a Senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem!")
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["senha"])
        if commit:
            usuario.save()
        return usuario

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Formulário de Login
class LoginForm(AuthenticationForm):
    pass  # Você pode personalizar isso, se necessário

# Formulário de Registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Campos do registro
