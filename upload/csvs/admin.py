from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Items

@admin.register(Items)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('category', 'prompts', 'keywords', 'cons', 'status')
    readonly_fields = ('category', 'prompts', 'keywords', 'cons')

