from django.shortcuts import render
from blog.data import posts
from django.http import Http404

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


def post(request, id):
    print('Post', id)

    found_post = None

    for post in posts:
        print(post)
        if post['id'] == id:
            found_post = post
            print(found_post)
            break

    if found_post is None:
        raise Http404('Post not found')
    
    context = {
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
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