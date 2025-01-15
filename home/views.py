from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    print('Home - Mostrando a home pra mim no cmd')
    return render(request,'home/index.html')