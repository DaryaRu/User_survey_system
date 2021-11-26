from django.contrib import admin
from survey.models.option import Option

class OptionAdmin(admin.ModelAdmin):
    list_display = ['question', 'text']
    list_filter = ['question']
    list_editable = ['text']
    
admin.site.register(Option, OptionAdmin)