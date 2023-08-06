from django.contrib import admin
from .models import New
from django_summernote.admin import SummernoteModelAdmin

from .models import Profile


@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'date_created' )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'date_created')
    summernote_fields = ('content')

 
admin.site.register(Profile)