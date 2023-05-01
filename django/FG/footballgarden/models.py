from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64, unique=True, default="Unknown")


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
