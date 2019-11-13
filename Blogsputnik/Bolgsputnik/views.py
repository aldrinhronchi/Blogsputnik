from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from Bolgsputnik.models import Posts
from django.contrib.auth import logout

@login_required
def postsList(request):
    postagens = Posts.objects.all()
    return render(request, 'posts.html', {'posts':postagens})

@login_required
def postsNew(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('postsList')
    return render(request, 'posts_form.html',{'form':form})

@login_required
def postsUpdate(request, id):
    posts = get_object_or_404(Posts, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=posts)
    if form.is_valid():
        form.save()
        return redirect('postsList')
    return render(request,'posts_form.html',{'form':form})

@login_required
def postsDelete(request, id):
    postagens = get_object_or_404(Posts, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=postagens)
    if request.method == 'POST':
        postagens.delete()
        return redirect('postsList')
    return render(request, 'posts_delete_confirm.html', {'posts':postagens})




class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo', 'texto','autor']


def home(request):

    return render(request, 'home.html')


def my_logout (request):
    logout(request)
    return redirect('home')
