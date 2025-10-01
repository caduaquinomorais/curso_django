from django.shortcuts import render


def home(request):
    print('Home - Mostrando a home pra mim no cmd')

    return render(request,'home/index.html')