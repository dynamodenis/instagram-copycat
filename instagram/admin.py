from django.contrib import admin
from .models import Image,Comments
# Register your models here.

class CommentInline(admin.TabularInline):
    model=Comments
    extra=3
    
class ImageInline(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['image']}),
        (None,{'fields':['image_name']}),
        (None,{'fields':['image_caption']}),
        (None,{'fields':['likes']}),
    ]
    inlines=[CommentInline]
    
    
admin.site.site_header='InstaPost Admin'
admin.site.site_title='InstaPost Admin Dashboard'

admin.site.register(Image,ImageInline)
# admin.site.register(Comments)
