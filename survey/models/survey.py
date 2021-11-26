from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()


    class Meta:
        db_table = 'surveys'
        ordering = ['start_date', 'end_date']

    def __str__(self):
        return self.title