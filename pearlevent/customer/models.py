from django.db import models
from django.contrib.auth.models import User
from event.models import Event
# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    eid=models.ForeignKey(Event, on_delete=models.CASCADE, db_column="eid")
    # oid=models.ForeignKey(Organizer, on_delete=models.CASCADE, db_column="oid")
 

