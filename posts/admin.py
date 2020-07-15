from django.contrib import admin

# Register models here.
from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    """Post fields that are displayed in the admin panel"""
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    """Group fields that are displayed in the admin panel"""
    list_display = ("title", "slug", "description")
    search_fields = ()
    list_filter = ()
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
