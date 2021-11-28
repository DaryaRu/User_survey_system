from django.db import models
from django.db.models.deletion import CASCADE
from .survey import Survey

class QuestionType(models.TextChoices):
    SINGLE = "SINGLE"
    MULTI = "MULTY"
    TEXT = "TEXT"

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QuestionType.choices)
    
    
    class Meta:
        db_table = 'questions'

    def __str__(self):
        return self.text                  