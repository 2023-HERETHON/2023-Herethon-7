from django.db import models

# Create your models here.
class Post (models.Model):
    place = models.TextField('동행할 여행지')