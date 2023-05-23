from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.order_by('-publication_date')
    return render(request,'blog/home.html',{'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request,'blog/create_post.html',{'form': form})
    
def view_post(request,pk):
    post = BlogPost.objects.get(id=pk)
    return render(request,'blog/view_post.html',{'post':post})

@login_required
def edit_post(request,pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,instance = post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request,'blog/edit_post.html',{'form':form,'post':post})


@login_required    
def delete_post(request,pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')