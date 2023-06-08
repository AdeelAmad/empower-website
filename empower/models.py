from django.db import models

# Create your models here.

class homePage(models.Model):
    whatwedo = models.TextField()
    mission = models.TextField()

class contactPage(models.Model):
    contactinfo = models.TextField()

class event(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.TextField()
    image = models.TextField()
    upcoming = models.BooleanField(default=False)

class image(models.Model):
    image = models.TextField()
    attribution = models.TextField()
    width = models.IntegerField()