from django.urls import path
from .views import home,PostList,PostDetail


urlpatterns = [
    # path('posts/',post_list, name='post_lists'),
    # path('posts/<int:post_id>',post_detail, name='post_details'),
    path('posts/',PostList.as_view(), name='PostList'),
    path('posts/<int:pk>',PostDetail.as_view(), name='PostDetail')
]