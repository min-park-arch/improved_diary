from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

def home (request):
  num = Blog.objects.count()
  return render (request, 'home.html', {'num':num})

@login_required(redirect_field_name=None, login_url="login")
def contents (request):
  blogs = Blog.objects.order_by('-pub_date')
  paginator = Paginator(blogs, 3)
  page = request.GET.get('page')
  blogs = paginator.get_page(page)
  return render (request, 'contents.html', {'blogs':blogs})

@login_required(redirect_field_name=None, login_url="login")
def detail (request,id):
  blog = get_object_or_404(Blog, pk = id)
  return render (request, 'detail.html', {'blog':blog})

@login_required(redirect_field_name=None, login_url="login")
def new (request):
  form = BlogForm ()
  return render (request, 'new.html', {'form': form})

@login_required(redirect_field_name=None, login_url="login")
def create (request):
  form = BlogForm(request.POST, request.FILES)
  if form.is_valid():
    new_blog = form.save(commit = False)
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect ('detail', new_blog.id)
  return redirect ('new')

@login_required(redirect_field_name=None, login_url="login")
def edit (request, id):
  edit_blog = Blog.objects.get (id = id)
  return render (request, 'edit.html', {'blog':edit_blog})

@login_required(redirect_field_name=None, login_url="login")
def update (request, id):
  update_blog = Blog.objects.get(id= id)
  update_blog.title = request.POST ['title']
  update_blog.body = request.POST ['body']
  update_blog.pub_date = timezone.now()
  update_blog.save()
  return redirect ('detail', update_blog.id)

@login_required(redirect_field_name=None, login_url="login")
def delete (request, id):
  delete_blog = Blog.objects.get(id=id)
  delete_blog.delete()
  return redirect('home')
