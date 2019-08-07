from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')


def create(request):
    name = request.GET.get('name')
    name_en = request.GET.get('name_en')
    category = request.GET.get('category')
    nation = request.GET.get('nation')
    replace = request.GET.get('replace')
    post = Post()
    post.name = name
    post.name_en = name_en
    post.category = category
    post.nation = nation
    post.replace = replace
    post.save()
    return redirect('/board/')

def detail(request, post_id):
    post = Post.objects.all().get(id=post_id)
    context = {
        'post': post     
    }
    return render(request, 'detail.html', context)
    

def edit(request, post_id):
    post = Post.objects.all().get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'edit.html', context)

def update(request, post_id):
    name = request.GET.get('name')
    name_en = request.GET.get('name_en')
    category = request.GET.get('category')
    nation = request.GET.get('nation')
    replace = request.GET.get('replace')
    
    post = Post.objects.all().get(id=post_id) 
    post.name = name
    post.name_en = name_en
    post.category = category
    post.nation = nation
    post.replace = replace
    post.save()
    return redirect('/board/')

def delete(request, post_id):
    post = Post.objects.all().get(id=post_id)
    post.delete()
    return redirect('/board/')