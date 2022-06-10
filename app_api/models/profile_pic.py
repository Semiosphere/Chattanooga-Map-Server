from django.db import models

class ProfilePic(models.Model):
    src = models.URLField()