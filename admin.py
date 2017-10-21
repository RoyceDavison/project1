from django.contrib import admin

# Register your models here.
from .models import User, Post, Comment, Video, Picture, Picture_post, Picture_comment, Video_post, Video_comment

#admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Picture)
admin.site.register(Picture_post)
admin.site.register(Picture_comment)
admin.site.register(Video_post)
admin.site.register(Video_comment)


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]



class PostInline(admin.TabularInline):
    model = Post

@admin.register(User)
class Userdmin(admin.ModelAdmin):
    inlines = [PostInline]
