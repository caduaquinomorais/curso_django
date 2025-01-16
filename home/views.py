from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    print('Home - Mostrando a home pra mim no cmd')
    
    context = {
    'text': 'Teste de tupla usando a função context',
        'title': 'Página de home'
}

    return render(request,'home/index.html',context,)