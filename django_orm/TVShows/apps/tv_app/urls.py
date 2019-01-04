from django.conf.urls import url
from . import views                
urlpatterns = [
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<id>\d+)$', views.display),
    url(r'^shows/show$',views.show), # use link ahref, instead of shows/show function --time saving
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<id>\d+)/update$', views.update),
    url(r'^shows/(?P<id>\d+)/delete$', views.delete)
    ]
