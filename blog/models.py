from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post", default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=Post)


# comments model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment", default=1)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
