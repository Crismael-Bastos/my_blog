from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from posts.models import Post


class Comment(models.Model):
    name_comment = models.CharField(max_length=150, verbose_name="Name")
    email_comment = models.EmailField(verbose_name="E-mail")
    comment = models.TextField(verbose_name="Comment")
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    date_comment = models.DateField(default=timezone.now)
    published_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.name_comment
