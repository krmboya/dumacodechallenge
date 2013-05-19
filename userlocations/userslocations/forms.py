from django import forms

from userprofile.models import Profile

users = ((profile.pk, "%s %s, %s" % 
          (profile.user.first_name, profile.user.last_name, profile.telephone_number))
         for profile in Profile.objects.all())

class MappingForm(forms.Form):
    county = forms.ChoiceField(choices=())
    ward = forms.ChoiceField(choices=())
    location = forms.ChoiceField(choices=())
    other = forms.CharField(required=False)


class UsersForm(forms.Form):
    user = forms.ChoiceField(choices=users)
