from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    tipo_sala = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero

class Chave(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)
    copias = models.IntegerField(default=1)

    def __str__(self):
        return self.codigo

class Autorizacao(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    sala_numero = models.CharField(max_length=10)
    motivo = models.TextField()
    data_retirada = models.DateTimeField()
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f"Autorização para {self.nome} - Sala {self.sala_numero}"

class SolicitacaoPosseChave(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    sala_numero = models.CharField(max_length=10)
    motivo_solicitacao = models.TextField()
    email = models.EmailField()
    data_solicitacao = models.DateTimeField()
    telefone = models.CharField(max_length=15)
    autorizacao = models.ForeignKey(Autorizacao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Solicitação de {self.nome} para {self.sala_numero}"

class Posse(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Posse de {self.usuario} - {self.chave}"

class StatusGeral(models.Model):
    historico_modificacoes = models.JSONField(default=list)  # Usando JSONField para armazenar o histórico de modificações
    autorizacao = models.ForeignKey(Autorizacao, on_delete=models.CASCADE)
    salas = models.ForeignKey(Sala, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    posse_chaves = models.ForeignKey(Posse, on_delete=models.CASCADE)
    chaves = models.ForeignKey(Chave, on_delete=models.CASCADE)

    def __str__(self):
        return f"Status Geral para {self.chaves}"
