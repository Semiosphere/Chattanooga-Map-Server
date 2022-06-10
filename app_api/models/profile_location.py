from django.db import models

class ProfileLocation(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)