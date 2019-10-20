from django.contrib import admin
from testapp.models import post,comments
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','create_on','update','status']
    list_filter=('status','author','create_on','publish')
    search_fields=('title','body')
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    raw_id_fields = ('author',)
    prepopulated_fields={'slug':('title',)}



class commentsadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'Post', 'body', 'created', 'updated', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(post,postadmin)
admin.site.register(comments,commentsadmin)