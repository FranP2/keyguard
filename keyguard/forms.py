from django import forms
from .models import Usuario, Sala, Chave, Autorizacao, Posse, StatusGeral,SolicitacaoPosseChave
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



# Formulário para o modelo Usuario
'''class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento', 'is_staff', 'is_superuser']'''

'''from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento', 'is_staff', 'is_superuser', 'password']
        widgets = {
            'is_staff': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user'''


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = [
            'nome', 'matricula', 'email', 'telefone', 
            'departamento', 'is_staff', 'is_superuser', 'password'
        ]
        widgets = {
            'is_staff': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password2"):
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Define is_staff baseado na lógica do email ou outro critério
        if user.email.endswith('@admin.com'):  # Exemplo: para marcar empresários
            user.is_staff = True
        else:
            user.is_staff = False  # Clientes padrão
        
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        return user





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
        widgets = {
            'usuario': forms.HiddenInput(),
        }


# Formulário para o modelo StatusGeral
class StatusGeralForm(forms.ModelForm):
    class Meta:
        model = StatusGeral
        fields = '__all__'

# Formulário de Registro de Usuário


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirma_senha = forms.CharField(widget=forms.PasswordInput, label="Confirme a senha")

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirma_senha = cleaned_data.get('confirma_senha')

        if password != confirma_senha:
            raise forms.ValidationError('As senhas não coincidem.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Criptografa a senha
        if commit:
            user.save()
        return user



# Formulário de Login
class LoginForm(AuthenticationForm):
    pass  # Você pode personalizar isso, se necessário

# Formulário de Registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Campos do registro


class SolicitacaoPosseChaveForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoPosseChave
        fields = ['nome', 'matricula', 'sala', 'motivo_solicitacao', 'email', 'telefone']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'matricula', 'email', 'telefone', 'departamento']
