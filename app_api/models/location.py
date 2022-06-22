from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    character_art = models.URLField()
    discovered_by = models.ManyToManyField("Profile", related_name="locations")
    x = models.IntegerField()
    y = models.IntegerField()
    profile_pic_id = models.ForeignKey("ProfilePic", on_delete=models.CASCADE)
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value