from django.db.models.signals import post_save
from django.shortcuts import render,get_object_or_404
from .models import  Author
# Create your views here.


def author_list(request):
    authors = Author.objects.all()
    return render(request,'author_list.html',{'authors':authors})


def author_detail(request,author_id):
    author = get_object_or_404(Author,id=author_id)
    posts = author.posts.all()
    return render(request,'author_detail.html',{'author':author,'posts':posts})