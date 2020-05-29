from django.contrib import admin
from .models import Image,Comments
# Register your models here.
admin.site.site_header='InstaPost Admin'
admin.site.site_title='InstaPost Admin Dashboard'

admin.site.register(Image)
admin.site.register(Comments)
