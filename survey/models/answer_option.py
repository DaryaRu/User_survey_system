from django.db import models
from django.db.models.deletion import CASCADE
from .answer import Answer
from .option import Option


class AnswerOption(models.Model):
    answer = models.ForeignKey(Answer, related_name='answer_options', on_delete=CASCADE)
    option = models.ForeignKey(Option, related_name='answer_options', on_delete=CASCADE) 
        
        
    class Meta:
        db_table = 'answer_options'