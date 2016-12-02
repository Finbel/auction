from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.front, name='front'),
	url(r'^update/$', views.update, name='update'),
	url(r'^buy/$', views.buy, name='buy'),
	url(r'^sell/$', views.sell, name='sell'),
]