from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Gerenciador personalizado
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O endereço de e-mail deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(email=email, nome=nome, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modelo de Usuário
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

# Modelo de Sala
class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    tipo_sala = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero

# Modelo de Chave
class Chave(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)
    copias = models.IntegerField(default=1)

    def __str__(self):
        return self.codigo

# Modelo de Autorização
class Autorizacao(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    motivo = models.TextField()
    data_retirada = models.DateTimeField()
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f"Autorização para {self.nome} - Sala {self.sala.numero}"

# Modelo de Solicitação de Posse de Chave
class SolicitacaoPosseChave(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    motivo_solicitacao = models.TextField()
    email = models.EmailField()
    data_solicitacao = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    autorizacao = models.ForeignKey(Autorizacao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Solicitação de {self.nome} para {self.sala.numero}"

# Modelo de Posse
class Posse(models.Model):
    usuario = models.ForeignKey('keyguard.Usuario', on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Posse de {self.usuario.nome} - {self.chave.codigo}"

# Modelo de Status Geral
class StatusGeral(models.Model):
    historico_modificacoes = models.JSONField(default=list)
    autorizacao = models.ForeignKey('Autorizacao', on_delete=models.CASCADE)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    usuario = models.ForeignKey('keyguard.Usuario', on_delete=models.CASCADE)
    posse_chaves = models.ForeignKey('Posse', on_delete=models.CASCADE)
    chave = models.ForeignKey('Chave', on_delete=models.CASCADE)

    def __str__(self):
        return f"Status Geral para Chave {self.chave.codigo}"
