from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    map_icon = models.URLField()
    character_art = models.URLField()
    discovered_by = models.ManyToManyField("Profile", related_name="locations")
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value