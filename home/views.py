from django.shortcuts import render

# Create your views here.
def home(request):
    print('Home')

    context = {
                    'text': 'Estamos na página Home'
                }
    return render(
                request,
                'home/home.html',
                context,
    )