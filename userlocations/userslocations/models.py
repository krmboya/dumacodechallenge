from django.db import models

from locations.models import Location
from userprofile.models import Profile

class Mapping(models.Model):
    profile = models.ForeignKey(Profile)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.profile.user.first_name + " - " + self.location.name
    

