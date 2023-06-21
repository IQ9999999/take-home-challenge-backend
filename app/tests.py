from django.test import TestCase, Client
from .models import Score

# Create your tests here.
class GetScoreTest(TestCase):
    def test_get_score(self):
        client = Client()
        # response = client.get('/get_score/?input=5&user_id=1')
        response = client.get('/get_score/?input=5&user_id=1&game_name=test_game') # new line
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 6)

        # Check if the score was saved in the database
        score = Score.objects.get(user_id=1)
        self.assertEqual(score.score, 6)
        self.assertEqual(score.game_name, 'test_game') # new line