from django.contrib import admin
from django import forms
from .models import Host, TestSuite


class HostAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name', 'ip_address', 'port')
    def __str__(self):
        return '%s' % self.name
    pass
admin.site.register(Host, HostAdmin)


class TestSuiteAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(TestSuiteAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'text':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
admin.site.register(TestSuite, TestSuiteAdmin)
