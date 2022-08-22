from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post
from .services import upload_image


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = (
        "id",
        "title_post",
        "author_post",
        "date_post",
        "category_post",
        "published_post",
    )
    list_editable = ("published_post",)
    list_display_links = (
        "id",
        "title_post",
    )
    summernote_fields = ("content_post",)

    def save_model(self, request, obj, form, change):
        if obj.image_post:
            image_url = upload_image(obj.image_post)
            obj.image_text = image_url
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
