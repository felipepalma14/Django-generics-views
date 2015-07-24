from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from crud.views import *

urlpatterns = [
	
    # Examples:
    # url(r'^$', 'axm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','crud.views.home',name='pagina_inicial'),

    url(r'^usuario/listar/$','crud.views.listar_usuarios',name='usuarios'),
    url(r'^usuario/criar/$',UsuarioForm.as_view(),name = 'criar_usuario'),
    url(r'^usuario/atualiza/(?P<pk>\d+)/$',UsuarioUpdade.as_view(),name='update_usuario'),
    url(r'^usuario/deleta/(?P<pk>\d+)/$',UsuarioDelete.as_view(),name='deletar_usuario'),


	url(r'^marca/criar/$',MarcaForm.as_view(),name = 'criar_marca'),
	url(r'^marca/listar/$','crud.views.listar_marcas',name='marcas'),
	url(r'^marca/atualiza/(?P<pk>\d+)/$',MarcaUpdate.as_view(),name='update_marca'),
    url(r'^marca/deleta/(?P<pk>\d+)/$',MarcaDelete.as_view(),name='deletar_marca'),

	url(r'^produto/criar/$',ProdutoForm.as_view(),name = 'criar_produto'),
	url(r'^produto/listar/$','crud.views.listar_produto',name='produtos'),
	url(r'^produto/atualiza/(?P<pk>\d+)/$',ProdutoUpdade.as_view(),name='update_produto'),
    url(r'^produto/deleta/(?P<pk>\d+)/$',ProdutoDelete.as_view(),name='deletar_produto'),

]
