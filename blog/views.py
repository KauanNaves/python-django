from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print('Home blog')
    return HttpResponse('Pagina Blog')


def exemplo(request):
    print('Exemplo')
    return HttpResponse('Pagina Exemplo')