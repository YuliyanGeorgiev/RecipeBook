from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    people = models.IntegerField(default=3)
    budget = models.IntegerField(default=12)
    image=models.FileField(null=True, blank=True)
    ingredients = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Choice(models.Model):
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

