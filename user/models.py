from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="", primary_key=True )
    password = models.CharField(max_length=255, default="")
    active = models.IntegerField(default=0)
    verify_link = models.CharField(max_length=255, default=0)
    log_in_time = models.CharField(max_length=255, default="")
    log_out_time = models.CharField(max_length=255, default="")

