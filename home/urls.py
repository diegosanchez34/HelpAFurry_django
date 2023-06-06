from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()