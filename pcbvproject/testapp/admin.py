from django.contrib import admin
from testapp.models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display = ['name','eno','sal','eaddr']

admin.site.register(student,studentadmin)