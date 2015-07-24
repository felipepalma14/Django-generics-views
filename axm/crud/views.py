from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from crud.models import *
from crud.forms import *


def home(request):
	#return HttpResponse("Bem vindo!!!")
	return render(request,'home.html')

def listar_usuarios(request):
	all_usuarios = Usuario.objects.all()
	search = request.GET.get('search_box')
	if search is not None:
		all_usuarios = all_usuarios.filter(nome__icontains= search)
	return render(request,'usuario/listar_usuario.html',{'all_usuarios':all_usuarios})


def detalhes_usuario(request,pk):
	usuario = Usuario.objects.get(pk=pk)
	return render(request,'usuario/detalhes_usuario.html',{'usuario':usuario})


class UsuarioForm(CreateView):
	template_name = 'usuario/usuario_form.html'
	model = Usuario

	fields = ['nome','email','senha','habilitado']
	

	def get_form(self,form_class):
		form = super(UsuarioForm,self).get_form(form_class)
		form.fields['senha'].widget = forms.PasswordInput()
		return form
	

class UsuarioUpdade(UpdateView):
    model = Usuario
    template_name = 'usuario/usuario_form.html'

    fields = ['nome','email','habilitado']

    success_url='/usuario/listar/'    

class UsuarioDelete(DeleteView):
	model = Usuario
	template_name = 'usuario/deletar_usuario.html'
	success_url ='/usuario/listar/'


class MarcaForm(CreateView):
	template_name = 'marca/marca_form.html'
	model = Marca
	fields=['nome']

def listar_marcas(request):
	all_marcas = Marca.objects.all()
	search = request.GET.get('search_box')
	if search is not None:
		all_marcas = all_marcas.filter(nome__icontains= search)
	return render(request,'marca/listar_marca.html',{'all_marcas':all_marcas})


class MarcaUpdate(UpdateView):
    model = Marca
    template_name = 'marca/marca_form.html'

    fields=['nome']

    success_url='/marca/listar/'    


class MarcaDelete(DeleteView):
	model = Marca
	template_name = 'marca/deletar_marca.html'
	success_url ='/marca/listar/'

def listar_marca(request):
	all_marcas = Marca.objects.all()
	search = request.GET.get('search_box')
	if search is not None:
		all_marcas = all_marcas.filter(nome__icontains= search)
	return render(request,'produto/listar_produto.html',{'all_marcas':all_marcas})



## Metodos Produto




class ProdutoForm(CreateView):
	template_name = 'produto/produto_form.html'
	model = Produto

	fields=['nome','preco','quantidade','usuario','marca']

def listar_produto(request):
	all_produtos = Produto.objects.all()
	search = request.GET.get('search_box')
	if search is not None:
		all_produtos = all_produtos.filter(nome__icontains= search)
	return render(request,'produto/listar_produto.html',{'all_produtos':all_produtos})


class ProdutoUpdade(UpdateView):
    model = Produto
    template_name = 'produto/produto_form.html'

    fields=['nome','preco','quantidade','usuario','marca']

    success_url='/produto/listar/'    


class ProdutoDelete(DeleteView):
	model = Produto
	template_name = 'produto/deletar_produto.html'
	success_url ='/produto/listar/'
