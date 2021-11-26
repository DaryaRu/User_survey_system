from django.db import models
from django.db.models.deletion import CASCADE
from .question import Question


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=CASCADE) 
    text = models.TextField()
    
        
    class Meta:
        db_table = 'options'