from django.contrib import admin
from survey.models.survey import Survey

class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date']
    list_filter = ['start_date']
    list_editable = ['description', 'end_date']
    
admin.site.register(Survey, SurveyAdmin)