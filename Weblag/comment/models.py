from django.db import models


from post.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
