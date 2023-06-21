from django.shortcuts import render
from django.http import JsonResponse
from .models import Score

# Create your views here.
def get_score(request):
    input_value = int(request.GET.get('input', 0))
    user_id = int(request.GET.get('user_id', 0))
    game_name = request.GET.get('game_name', None) # new line
    result = input_value + 1

    # Save the score to the database
    # score = Score(user_id=user_id, score=result)
    score = Score(user_id=user_id, score=result, game_name=game_name) # new line
    score.save()

    return JsonResponse({'result': result})