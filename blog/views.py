from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts
# Create your views here.

def blog(request):
    print('Blog - Mostrando a home blog pra mim no cmd')

    context = {
        #'text': 'usando o context para fazer o texto do blog',
        'posts': posts
    }
    return render(
        request, 
        'blog/index.html',
        context
    )

def post(request, id):
    print('Post - Mostrando a home blog pra mim no cmd', id)

    context = {
        #'text': 'usando o context para fazer o texto do blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('Exemplo - Mostrando a home pra mim no cmd')

    context = {
        'text': 'usando o context para fazer o texto do exemplo',
        'title': 'Página de exemplo'
    }
    return render(request, 'blog/exemplo.html',context,)