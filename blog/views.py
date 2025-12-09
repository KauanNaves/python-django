from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts

# Create your views here.
def home(request):
    print('Home blog')
    context = {
                    'posts': posts
                }
    return render(
                request,
                'blog/home.html',
                context
    )


def exemplo(request):
    print('Exemplo')
    context = {
                    'text': 'Estamos na página Exemplo blog'
                }
    return render(
                request,
                'blog/exemplo.html',
                context)  