
from django.db import models	
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
# Create your models here.

'''
Ler abstractBaseUser para autenticacao
'''

alphanumeric = RegexValidator(r'^[a-zA-Z ]*$','Only letters are allowed')

class Usuario(models.Model):
	nome = models.CharField(max_length =60,null=False)
	email = models.EmailField(max_length=40,null=False,unique=True)
	senha = models.CharField(max_length=600,null=False)
	habilitado = models.BooleanField()

	def __unicode__(self):
		return u'{0}'.format(self.nome)

	def get_absolute_url(self):
		return reverse('usuarios')

class Marca(models.Model):
	nome = models.CharField(max_length=60,null=False)

	def __unicode__(self):
		return u'{0}'.format(self.nome)

	def get_absolute_url(self):
		return reverse('marcas')

class Produto(models.Model):
	nome  = models.CharField(max_length=60,null=False)
	preco = models.FloatField()
	quantidade = models.IntegerField()

	usuario = models.ForeignKey(Usuario)
	marca = models.ForeignKey(Marca)

	def __unicode__(self):
		return u'{0}'.format(self.nome)

	def get_absolute_url(self):
		return reverse('produtos')
