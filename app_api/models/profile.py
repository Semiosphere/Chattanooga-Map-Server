from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_pic = models.ForeignKey("ProfilePic", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)