from django.db import models
from django.core.mail import send_mail

from locations.models import Location, Ward
from userprofile.models import Profile
from userlocations.settings import EMAIL_RECEPIENT

class MappingManager(models.Manager):
    def add_location(self, name, profile):
        matches = Location.objects.filter(name__iexact=name)
        if matches:
            location = matches[0]
        else:
            location = Location(name=name,
                                ward=Ward.objects.get(name__iexact='other'))
            location.save()
            user_name = "%s %s" % (profile.user.first_name, profile.user.last_name)
            subject = 'New location added'
            body = "Dear Eric, a user called %s added an unfamiliar location called '%s'." % (user_name, name)
            fro = 'noreply@localhost'
            to = EMAIL_RECEPIENT
            send_mail(subject, body, fro, [to, 'krmboya@gmail.com'], fail_silently=False)
        mapping = Mapping(
            profile=profile,
            location=location)
        mapping.save()
        return mapping


class Mapping(models.Model):
    profile = models.ForeignKey(Profile)
    location = models.ForeignKey(Location)
    objects = MappingManager()

    def __unicode__(self):
        return self.profile.user.first_name + " - " + self.location.name
    

