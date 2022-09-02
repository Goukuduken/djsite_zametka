from django.contrib import admin
from .models import *
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','text','time_create')
    search_fields = ('title', 'text')

admin.site.register(Notice, NoticeAdmin)