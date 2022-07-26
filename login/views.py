from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def comCDN(request):
    return render(request, 'login/cdn.html')

def estatico(request):
    return render(request, 'login/estatico.html')