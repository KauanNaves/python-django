from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print('Home blog')
    return render(request,
                  'blog/home.html'
    )


def exemplo(request):
    print('Exemplo')
    return render(request, 'blog/exemplo.html')  