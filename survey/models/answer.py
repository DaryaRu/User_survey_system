from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from .question import Question

User = get_user_model()

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=CASCADE) 
    text = models.TextField()
    
        
    class Meta:
        db_table = 'answers'
                
    def __str__(self):
        return self.name