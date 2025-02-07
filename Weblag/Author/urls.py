from django.urls import path
from .views import author_list,author_detail


urlpatterns = [
    path('authors/',author_list, name='author_list'),
    path('authors/,int:post_id>',author_detail, name='author_detail'),
]