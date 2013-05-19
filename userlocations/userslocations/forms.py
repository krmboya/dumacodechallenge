from django import forms

from userprofile.models import Profile
from locations.models import County, Ward, Location

users = ((profile.pk, "%s %s, %s" % 
          (profile.user.first_name, profile.user.last_name, profile.telephone_number))
         for profile in Profile.objects.all())

counties = ((county.pk, "%s" % 
             county.name)
            for county in County.objects.all())

class BaseForm(forms.Form):
    other = forms.CharField(required=False)

class CountyForm(BaseForm):
    county = forms.ChoiceField(choices=counties, required=False)

class UsersForm(forms.Form):
    user = forms.ChoiceField(choices=users, required=True)


def get_ward_form(county):
    wards = ((ward.pk, "%s, %s" % 
              (ward.name, ward.county.name))
             for ward in Ward.objects.filter(county=county))

    class WardForm(BaseForm):
        ward = forms.ChoiceField(choices=wards, required=False)
        
    return WardForm

def get_location_form(ward):
    locations = ((location.pk, "%s, %s" % 
                  (location.name, location.ward.county.name))
                 for location in Location.objects.filter(ward=ward))
    
    class LocationForm(BaseForm):
        location = forms.ChoiceField(choices=locations, required=False)
        
    return LocationForm
