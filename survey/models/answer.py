from django.db import models
from django.db.models.deletion import CASCADE

from survey.models.option import Option
from .question import Question
from .anonymous_user import AnonymousUser

class Answer(models.Model):
    user = models.ForeignKey(AnonymousUser, related_name='answers', on_delete=CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=CASCADE) 
    text = models.TextField(blank=True)
    selected_options = models.ManyToManyField(Option)
    
        
    class Meta:
        db_table = 'answers'