from django.test import TestCase
from .models import Complication,Feedback,Profile

# Create your tests here.
class ComplicationTestClass(TestCase):

    def setUp(self):
        self.new_complication= Complication(title = 'Test complication',complication = 'This is a random test complication')
        self.new_complication.save()

    def tearDown(self):
        Complication.objects.all().delete()

class FeedbackTestClass(TestCase):

    # def setUp(self):
    #     self.new_post= Help(title = 'Test help',help = 'This is a random test help')
    #     self.new_post.save()

    def tearDown(self):
        Feedback.objects.all().delete()

class ProfileTestClass(TestCase):

    # def setUp(self):
    #     self.new_profile= Profile(title = 'Test profile',profile = 'This is a random test Profile')
    #     self.new_profile.save()


    def tearDown(self):
        Profile.objects.all().delete()