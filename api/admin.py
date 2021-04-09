from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','created_at','updated_at','owner']
    list_filters=['title','owner']
admin.site.register(Post,PostAdmin)
