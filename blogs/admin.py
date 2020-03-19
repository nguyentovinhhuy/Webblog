from django.contrib import admin
from .models import Author, BlogPost, Comments

# Register your models here.
'''class BlogsInline (admin.TabularInline):
    model = BlogPost
    extra = 5

class AuthorAdmin (admin.ModelAdmin):
    fieldsets = [
    
    ]

admin.site.register (BlogsInline, AuthorAdmin)'''