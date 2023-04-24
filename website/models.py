from django.db import models

class contato(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    mensagem = models.TextField()
    # recebernoticias = models.BooleanField()
    # email = models.EmailField()
    
    def __str__(self):
        return self.nome