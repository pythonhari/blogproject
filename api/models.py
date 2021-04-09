from django.db import models

# Create your models here.
class Post(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=256,unique=True,blank=False)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    owner=models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)

    class Meta:
        ordering=['created_at']

class comment(models.Model):
    id=models.IntegerField(primary_key=True)
    description=models.TextField(blank=True)
    owner=models.ForeignKey('auth.User',related_name='comments',on_delete=models.CASCADE)
    post=models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
