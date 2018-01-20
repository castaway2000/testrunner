from django.contrib import admin
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
from .models import Host, PageContent


class HostAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name', 'ip_address', 'port')
    def __str__(self):
        return '%s' % self.name
    pass
admin.site.register(Host, HostAdmin)


# Apply summernote to all TextField in model.
class PageContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summer_note_fields = '__all__'
admin.site.register(PageContent, PageContentAdmin)