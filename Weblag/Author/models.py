from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(User):
   bool = models.TextField(blank=True,null=True)
   is_admin = models.BooleanField(default=True)