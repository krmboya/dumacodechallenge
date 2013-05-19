from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from userprofile.models import Profile
from locations.models import County, Ward, Location

import forms
import models

def select_user(request, template_name='select_option.html'):
    if request.method == 'POST':
        form = forms.UsersForm(request.POST)
        if form.is_valid():
            profile_id = int(form.cleaned_data['user'])
            profile = get_object_or_404(Profile, pk=profile_id)
            request.session['user_profile'] = profile
            return HttpResponseRedirect(reverse(select_location))
    elif request.method == 'GET':
        form = forms.UsersForm()
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=RequestContext(request))
                              

def select_location(request, template_name='select_location.html'):
    label = ''
    if request.method == 'POST':
        if request.POST.get('county'):
            form = forms.CountyForm(request.POST)
            if form.is_valid():
                county = get_object_or_404(County, pk=int(form.cleaned_data['county']))
                form = forms.get_ward_form(county)
                label = 'ward'
    if request.method == 'GET':
        form = forms.CountyForm()
        label = 'county'
    return render_to_response(template_name,
                              {'form': form,
                               'label': label},
                              context_instance=RequestContext(request))
