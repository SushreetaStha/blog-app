from django.contrib import admin
from blog.models import Category,Tags,Image,Blog
# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Image)
admin.site.register(Blog)
