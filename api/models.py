from django.db import models

class Blog(models.Model):
    blogId = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=20)
    madeOn = models.DateTimeField(auto_now_add=True)

