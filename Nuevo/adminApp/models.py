from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255)
    experience = models.IntegerField()
    skills = models.TextField()
    cultural_fit = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    resume_path = models.CharField(null=True, blank=True, max_length=255)
