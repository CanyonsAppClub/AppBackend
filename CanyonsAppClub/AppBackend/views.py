# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from AppBackend.models import CalendarEvent, AppUser
from AppBackend.models import EventLocation
from AppBackend.models import Announcement

#from itertools import izip
from django.core import serializers


def home(request):
    calendar_events = CalendarEvent.objects.all().order_by('start_date')
    return render(request, 'welcome.html', {'events': calendar_events})


def announcement(request):
    return render(request, 'announcements.html', {"announcements": Announcement.objects.all()})


def loc_test(request):
    #jsonDecoder = json.JSONEncoder()
    # event_title =
    # event_subtitle
    # start_date =
    # end_date =
    location = CalendarEvent.objects.all()
    return render(request, 'encoding-test.json', {'locations': location})


def count(request):
    users = User.objects.filter()
    return render(request, 'counter-example.html', {'users': users})

# This code is no longer used, kept here for reference
# def list_files(request):
#     if request.method == 'POST':
#         form = LocationIconForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_icon = LocationIcon(icon_file = request.FILES['icon_file'])
#             new_icon.save(force_update=True)
#             return HttpResponseRedirect(reverse('AppBackend.views.list_files'))
#     else:
#         form = LocationIconForm()
#
#     icons = LocationIcon.objects.all()
#
#     return render_to_response(
#         'list-files.html',
#         {'icons': icons, 'form': form},
#         context_instance=RequestContext(request)
#     )
#
# def app_calendar_list(request):
#     calendar_events = CalendarEvent.objects.all()
#     return render(request, 'calendar-event.json', { 'events': calendar_events })
#
# def app_location_icon(reqeust):
#     event_locations = EventLocation.objects.all()
#     return render(reqeust, 'icon-reference.json', { 'locations': event_locations })


def app_json_event_list(request):
    return HttpResponse(serializers.serialize("json", CalendarEvent.objects.all()), mimetype='application/json')


def app_json_location_list(request):
    return HttpResponse(serializers.serialize("json", EventLocation.objects.all()), mimetype='application/json')


def app_json_robust_event_list(request):
    return render(request, 'event_summary.json', {'events': CalendarEvent.objects.all()}, content_type="application/json")

def app_json_robust_announcement_list(request):
    return render(request, 'announcements.json', {'announcements': Announcement.objects.all()}, content_type="application/json")


def app_json_announcement_list(request):
    return HttpResponse(serializers.serialize("json", Announcement.objects.order_by('-creation_date').all()), mimetype='application/json')


def username_from_id(request):
    if request.method == 'GET':
        user_id = request.GET.get('userid')
        user = User.objects.get(pk=user_id)
        response_data = '[{\"username\": \"' +\
                        user.username +'\",\"first_name\":\"' +\
                        user.first_name + '\",\"last_name\":\"' +\
                        user.last_name + '\",\"email\":\"' +\
                        user.email +\
                        '\"}]'
    return HttpResponse(response_data, mimetype='application/json')


def app_json_users_list(request):

    return HttpResponse(serializers.serialize("json", User.objects.all()), mimetype='application/json')

# def app_json_icon_list(request):
#     return HttpResponse(serializers.serialize("json", LocationIcon.objects.all()), mimetype='application/json')


def user_login(request):
    notwelcome = {}
    if request.method == 'POST':
        if request.POST.has_key('logout'):
            logout(request)
        else:
            #Login
            username = request.POST['username']
            password = request.POST['password']
            activeUser = authenticate(username=username, password=password)
            if activeUser is not None:
                if activeUser.is_active:
                    login(request, activeUser)
                    if 'next' in request.GET.keys():
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect("/manage/events/")
                else:
                    notwelcome['disabled'] = 'This account has been disabled.'
            else:
                notwelcome['invalid'] = "Invalid username or password"
    return render(request, "login.html", {'problems': notwelcome})

@permission_required('Edit Events and Locations', login_url='/login/')
def manage_events(request):
    if request.method == 'POST':
        dead_events = request.POST.keys()
        listing = ""
        for event in dead_events:
            if 'selected-event-' in event:
                CalendarEvent.objects.get(pk=str(event).split("-")[-1]).delete()
        return HttpResponseRedirect("/manage/events/")
        #return HttpResponse("<html><body>" + listing + "</body></html>")
    else:
        calendar_events = CalendarEvent.objects.all()
        locations = EventLocation.objects.all()
        return render(request, 'manage-events.html', {'events': calendar_events, 'locations': locations})


def manage_locations(request):
    locations = EventLocation.objects.all()
    return render(request, 'manage-locations.html', {'locations': locations})


def debug_view(request):
    #uncooked_models = CalendarEvent.objects.all()
    #location = CalendarEvent.
    #return HttpResponse(serializers.serialize("json", location), mimetype='application/json')
    #return HttpResponse(serializers.serialize("json", CalendarEvent.objects.all()), mimetype='application/json')
    sysargs = sys.argv
    #sysargs.insert(1, "_meta", "nothing")
    #sysargs.in
    return render(request, 'debug.html', {'debug_items': sysargs})
    #return HttpResponse(serializers.serialize("json", sysargs), mimetype='application/json')