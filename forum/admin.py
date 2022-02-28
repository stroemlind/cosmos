from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    """
    A class to prepopulate slug-fileds
    """
    list_display = ('title', 'author', 'category')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Handling comment from the admin panel
    """
    list_display = ('user', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function to approve comments
        """
        queryset.update(approved=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
