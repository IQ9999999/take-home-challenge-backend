from django.contrib import admin
from .models import Score

# Register your models here.

class ScoreAdmin(admin.ModelAdmin): # new line
    list_display = ('user_id', 'game_name', 'score') # new line

# admin.site.register(Score)
admin.site.register(Score, ScoreAdmin) # new line