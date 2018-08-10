from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404

from .models import BlogPost
from .forms import NewPostForm

# Create your views here.

def index(request):
    """主页"""
    posts=BlogPost.objects.order_by('-date_added')
    
    context={'posts':posts}
    return render(request,'blogs/index.html',context)

@login_required    
def new_post(request):
    """发布新帖子"""
    if request.method != 'POST':
        form=NewPostForm()
    else:
        form=NewPostForm(request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.owner=request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
            
    context={'form':form}
    return render(request,'blogs/new_post.html',context)

@login_required
def edit_post(request,post_id):
    """编辑既有的帖子"""
    post=BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form=NewPostForm(instance=post)
    else:
        form=NewPostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
            
    context={'post':post,'form':form}
    return render(request,'blogs/edit_post.html',context)
