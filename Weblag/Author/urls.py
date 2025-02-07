from django.urls import path
from .views import AuthorDetail,AuthorList


urlpatterns = [
    # path('authors/',author_list, name='author_lists'),
    # path('authors/<int:author_id>',author_detail, name='author_details'),
    path('authors/',AuthorList.as_view(), name='AuthorList'),
    path('authors/<int:pk>',AuthorDetail.as_view(), name='AuthorDetail'),
]