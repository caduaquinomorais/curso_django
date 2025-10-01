from django.shortcuts import render
from django.http import Http404, HttpResponse
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

def post(request, post_id):
    print('Post - Mostrando a home blog pra mim no cmd', id)
    found_post: dict[str, any] = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    return render(
        request,
        'blog/post.html',
        context
    )

def exemplo(request):
    print('Exemplo - Mostrando a home pra mim no cmd')

    context = {
        'text': 'usando o context para fazer o texto do exemplo',
        'title': 'Página de exemplo'
    }
    return render(request, 'blog/exemplo.html',context,)