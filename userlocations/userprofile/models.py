from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    telephone_number = models.CharField(max_length=255)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.first_name + " " + self.telephone_number
                                        
