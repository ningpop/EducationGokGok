from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0, null=True)
    felmale = models.BooleanField(default = True)
    phone = models.CharField(max_length=20)
