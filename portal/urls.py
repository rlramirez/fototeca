from django.conf.urls import include, url, patterns
from . import views
#from django.contrib.auth.views import login
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


urlpatterns = patterns('portal.views',
	url(r'^$', 'home_page', name='home'),
	url(r'^formulario/$',login, {'template_name':'internas/formulario.html'}, name='login'),
	#url(r'^logout/$', logout, {'template_name': 'internas/logout.html'}, name='logout'),
	url(r'^logout/$', 'logout_view', name='logout_view'),
	url(r'^reconoce/$', 'listado_fotos', name='listado_fotos'),
	url(r'foto/(?P<id>\d+)$', views.foto, name='foto'),
	#url(r'^api/sacardata$', 'sacar_data', name='sacar_data'),
	#url(r'^api/sacarlugares$', 'listarlugares', name='json'),
	#url(r'^mapa', 'mapa_view', name='mapa'),
	#url(r'^estadistica', 'estadistica_view', name='estadistica'),
	#url(r'^tablas', 'data_table', name='tables'),
	)