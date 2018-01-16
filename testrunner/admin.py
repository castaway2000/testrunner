from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PageContent


# Apply summernote to all TextField in model.
class PageContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summer_note_fields = '__all__'

admin.site.register(PageContent, PageContentAdmin)