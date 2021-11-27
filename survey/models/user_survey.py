from django.db import models
from .anonymous_user import AnonymousUser
from django.db.models.deletion import CASCADE
from .survey import Survey

class UserSurvey(models.Model):
    user = models.ForeignKey(AnonymousUser, related_name='user_surveys', on_delete=CASCADE)
    survey = models.ForeignKey(Survey, related_name='user_surveys', on_delete=CASCADE) 
        
        
    class Meta:
        db_table = 'user_surveys'