from django.contrib import admin
from .models import Post , Tag , Comment ,AuthorProfile
# Register your models here.

admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Comment)
admin.site.register(AuthorProfile)