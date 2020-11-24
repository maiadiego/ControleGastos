from django.db import models
# models descrevem as tabelas do banco de dados, as quais possuem atributos, que são os fields
# todo model do django herda da model, que é a classe pai de todas as models


class Categoria(models.Model):
    objects = None
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    objects = None
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    # definindo o nome no plural
    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self): # self se refere a própria classe transação
        return self.descricao # mostrar o campo 'descricao' ao invés do object padrão django