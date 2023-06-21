from django.db import models

# Create your models here.
class Score(models.Model):
    user_id = models.IntegerField()
    score = models.IntegerField()
    game_name = models.CharField(max_length=200, null=True)  # new line