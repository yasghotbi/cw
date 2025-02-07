from django.urls import path
from .views import author_list,author_detail


urlpatterns = [
    path('authors/',author_list, name='author_lists'),
    path('authors/<int:author_id>',author_detail, name='author_details'),
]