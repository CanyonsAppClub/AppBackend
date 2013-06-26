from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import LocationIconForm
from django.contrib.auth.models import User

from django.shortcuts import render

from AppBackend.models import LocationIcon
from AppBackend.forms import LocationIconForm

from AppBackend.models import CalendarEvent
from AppBackend.models import EventLocation
import json
import sys

from django.core import serializers


def home(request):
    calendar_events = CalendarEvent.objects.all()
    return render(request, 'welcome.html', { 'events': calendar_events })

def loc_test(request):
    #jsonDecoder = json.JSONEncoder()
    # event_title =
    # event_subtitle
    # start_date =
    # end_date =
    location = CalendarEvent.objects.all()
    return render(request, 'encoding-test.json', { 'locations' : location })

def count(request):
    users = User.objects.filter()
    return render(request, 'counter-example.html', {'users': users})

def list_files(request):
    if request.method == 'POST':
        form = LocationIconForm(request.POST, request.FILES)
        if form.is_valid():
            new_icon = LocationIcon(icon_file = request.FILES['icon_file'])
            new_icon.save(force_update=True)
            return HttpResponseRedirect(reverse('AppBackend.views.list_files'))
    else:
        form = LocationIconForm()

    icons = LocationIcon.objects.all()

    return render_to_response(
        'list-files.html',
        {'icons': icons, 'form': form},
        context_instance=RequestContext(request)
    )

def app_calendar_list(request):
    calendar_events = CalendarEvent.objects.all()
    return render(request, 'calendar-event.json', { 'events': calendar_events })

def app_location_icon(reqeust):
    event_locations = EventLocation.objects.all()
    return render(reqeust, 'icon-reference.json', { 'locations': event_locations })

def debug_view(request):
    #uncooked_models = CalendarEvent.objects.all()
    #location = CalendarEvent.
    #return HttpResponse(serializers.serialize("json", location), mimetype='application/json')
    #return HttpResponse(serializers.serialize("json", CalendarEvent.objects.all()), mimetype='application/json')
    sysargs = sys.argv
    return render(request, 'debug.html', { 'debug_items':sysargs})