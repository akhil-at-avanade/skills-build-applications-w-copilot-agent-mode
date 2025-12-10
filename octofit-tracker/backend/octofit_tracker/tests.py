from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-01-01')
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
