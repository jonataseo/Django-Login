from django.urls import path

from . import views

urlpatterns = [
    # ex: /login/
    path('', views.index, name='index')
]