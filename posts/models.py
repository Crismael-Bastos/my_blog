import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

from categories.models import Category


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name="Title")
    author_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Author"
    )
    date_post = models.DateTimeField(default=timezone.now, verbose_name="Date")
    content_post = models.TextField(verbose_name="Content")
    excerpt_post = models.TextField(verbose_name="Excert")
    category_post = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name="Category",
    )
    image_post = models.ImageField(
        upload_to="post_img/%Y/%m/%d", blank=True, null=True, verbose_name="Image"
    )
    published_post = models.BooleanField(default=False, verbose_name="Published")
    image_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image_post:
            self.image_post = None
