__author__ = 'jorge'
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from blog import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^entrada/(\d+)/$', views.entrada, name='entrada'),
    url(r'^month/(\d+)/(\d+)/$', views.month, name='month'),
    url(r'main', views.main, name='main'),
    url(r'^poncomentario/(\d+)/$',views.comentario, name='poncomentario'),

]
