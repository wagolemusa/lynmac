from django.contrib import admin
# Register your models here.
from .models import Post, Images

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post 
		
class ImagesAdmin(admin.ModelAdmin):
	list_display = ["post", "image"]

admin.site.register(Post, PostModelAdmin)
admin.site.register(Images, ImagesAdmin)