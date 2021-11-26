from django.contrib import admin
from survey.models.question import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['survey', 'text', 'question_type']
    list_filter = ['question_type']
    list_editable = ['text', 'question_type']
    
admin.site.register(Question, QuestionAdmin)