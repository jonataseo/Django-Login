from django.urls import path

from . import views

urlpatterns = [
    # ex: /login/
    path('', views.index, name='index'),
    path('cdn', views.comCDN, name='comCDN'),
    path('estatico', views.estatico, name='estatico')
]