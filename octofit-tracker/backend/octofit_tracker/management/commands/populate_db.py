from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc),
            User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc),
        ]

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        workout2 = Workout.objects.create(name='Flight Training', description='Flight skills and endurance')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create activities
        Activity.objects.create(user=users[0], type='Iron Suit Training', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Kryptonian Flight', duration=45, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[3], score=95)
        Leaderboard.objects.create(user=users[4], score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
