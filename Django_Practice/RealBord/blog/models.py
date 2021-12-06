from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tag(models.Model):
    slug = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.slug



class Article(models.Model):
    title = models.CharField(default="",  max_length=30)
    text = models.TextField(default="")
    author = models.CharField(default="", max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )