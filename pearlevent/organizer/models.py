from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organizer(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    uid=models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    


    