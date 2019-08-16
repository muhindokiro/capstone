from django.contrib.auth.models import User
from django.db import models
import datetime as dt

# Create your models here.

# Complication class.
class Complication(models.Model):
    complication_name = models.CharField(max_length =60)
    symptoms = models.CharField(max_length =200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def index(cls):
        complication = cls.objects.filter()
        return complication

    @classmethod
    def search_by_complication_name(cls,search_term):
        complication = cls.objects.filter(complication_name__icontains=search_term)
        return complication

# Feedback class.
class Feedback(models.Model):
    feedback = models.CharField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def index(cls):
        feedback = cls.objects.filter()
        return feedback
    
# Profile class.
class Profile(models.Model):
    bio = models.CharField(max_length =60)
    contact = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile/', blank=True)

    @classmethod
    def profile(cls):
        profile = cls.objects.filter()
        return profile

    def save_profile(self):
        self.save()
