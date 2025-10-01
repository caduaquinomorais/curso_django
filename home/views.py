from django.shortcuts import render


def home(request):
    print('Home - Mostrando a home pra mim no cmd')
    
    context = {
        'text': 'Teste de tupla usando a função context'
    }

    return render(request,'home/index.html',context,)