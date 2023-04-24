from django.db import models
import math

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=15)
    cor = models.CharField(max_length=50)
    obs = models.TextField()
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.placa
    
class Parametros(models.Model):
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
        
    def __str__(self):
        return "Valores Padrões"
    
class movRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=6, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)
    
    def horas_total(self):
        try:
            return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)
        except:
            pass
 
    def total(self):
        try:
            return self.valor_hora * self.horas_total()
        except:
            pass
    
    def __str__(self):
        return self.veiculo.placa
    
class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    mensalista = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.veiculo)
    
class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.mensalista) + ' + ' + str(self.total)