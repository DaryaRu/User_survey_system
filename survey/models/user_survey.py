from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from .survey import Survey

User = get_user_model()

class UserSurvey(models.Model):
    user = models.ForeignKey(User, related_name='user_surveys', on_delete=CASCADE)
    question = models.ForeignKey(Survey, related_name='user_surveys', on_delete=CASCADE) 
        
        
    class Meta:
        db_table = 'user_surveys'