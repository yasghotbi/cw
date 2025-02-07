from django.db import models

class ContactusMessage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_ad = models.DateTimeField(auto_now_add=True)
