from django.urls import path
from .views import post_list,post_detail,home


urlpatterns = [
    path('posts/',post_list, name='post_lists'),
    path('posts/<int:post_id>',post_detail, name='post_details'),
]