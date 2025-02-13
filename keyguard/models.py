from django.db import models



class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.numero

class Chave(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificador

class Autorizacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_autorizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Autorização para {self.usuario} - {self.chave}"


class Posse(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField(auto_now_add=True, editable=False)
    data_devolucao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Posse de {self.usuario} - {self.chave}"


class StatusGeral(models.Model):
    chave = models.OneToOneField(Chave, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"Status {self.chave}: {'Disponível' if self.disponivel else 'Indisponível'}"
