from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    print('Blog - Mostrando a home pra mim no cmd')
    return render(request, 'blog/index.html')

def exemplo(request):
    print('Exemplo - Mostrando a home pra mim no cmd')
    return render(request, 'blog/exemplo.html')