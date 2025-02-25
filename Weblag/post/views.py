from django.db.models.signals import post_save
from django.shortcuts import render,get_object_or_404
from .models import  Post
from .apps import PostConfig
from django.views import View
# Create your views here.



def home(request):
    latest_posts = Post.objects.order_by('-published_date')[:3]
    return render(request, 'home.html', {'latest_post': latest_posts})

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request,'post_list.html',{'posts':posts})
#
#
# def post_detail(request,post_id):
#     post = get_object_or_404(Post,id=post_id)
#     return render(request,'post_detail.html',{'post':post})


class PostList(View):
    def get(self, request,*args,**kwargs):
        posts = Post.objects.all()
        return render(request,'post_list.html',{'posts':posts})

class PostDetail(View):
    def get(self, request,*args,**kwargs):
        post_id=kwargs["pk"]
        post = get_object_or_404(Post,id=post_id)
        return render(request,'post_detail.html',{'post':post})