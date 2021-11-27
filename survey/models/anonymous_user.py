from django.db import models

class AnonymousUser(models.Model):
    
    class Meta:
        db_table = 'anonymous_users'

    def __str__(self):
        return str(self.id)