from django.db import models
from django.contrib.auth.models import User

from organizer.models import Organizer


# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to="event_images")
    name= models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    startdate=models.DateField()
    enddate=models.DateField()
    eventlocation=models.CharField(max_length=50)
    price = models.FloatField()
    eventdescription=models.CharField(max_length=50)
    uid=models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
