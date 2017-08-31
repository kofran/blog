from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import PostForm, CommentForm, SignUpForm
from .decorators import check_recaptcha
# Create your views here.

def home(request):
    posts = (Post.objects.filter(published_date__lte=timezone.now()).
            order_by('published_date').reverse())
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(postid=pk)
    form = CommentForm(request.POST,)

    if form.is_valid():

        comment = form.save(commit=False)
        comment.author = request.user
        comment.postid = Post.objects.get(pk=pk)
        comment.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required(login_url='/login')
@permission_required('post.can_add', login_url='/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/login')
@permission_required('post.can_change', login_url='/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def login(request):
    return render(request, 'blog/login.html', {})

@check_recaptcha
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # messages.success(request, 'New comment added with success!')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
