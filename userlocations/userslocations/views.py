from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

import forms
import models

def select_user(request, template_name='select_option.html'):
    form = forms.UsersForm()
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=RequestContext(request))
                              

def select_location(request, template_name='select_location.html'):
    form = forms.MappingForm()
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=RequestContext(request))
