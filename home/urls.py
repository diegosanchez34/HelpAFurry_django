from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index', views.index, name='index'),
    path('contactanos',views.contactanos,name='contactanos'),
    path('crearusuario',views.crearusuario,name='crearusuario'),
    path('gatos',views.gatos,name='gatos'),
    path('login',views.login,name='login'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('perros',views.perros,name='perros'),
    path('singin',views.singin,name='singin'),
]

urlpatterns += staticfiles_urlpatterns()