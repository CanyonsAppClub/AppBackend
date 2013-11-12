from django.forms.extras.widgets import SelectDateWidget
from django.db import models
#from django.forms import forms, DateField
from django.contrib.auth.models import User
from datetime import datetime

# import json
# from django.utils.functional import Promise
# from django.utils.encoding import force_text
# from django.core.serializers.json import DjangoJSONEncoder

# class SchoolIndex:
#     schooldictionary = {
#         'schools' : (
#             ('0','Alta'),
#             ('1','Brighton'),
#             ('2','Corner Canyon'),
#             ('3','Hillcrest'),
#             ('4','Jordan')
#         )
#     }

# class LazyEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Promise):
#             return force_text(obj)
#         return super(LazyEncoder, self).default(obj)

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(date_format, t):
    return t.strftime(date_format).replace('{S}', str(t.day) + suffix(t.day))



class AppUser(models.Model):
    user = models.ForeignKey(User)
    #email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            display_text = self.user.first_name + " " + self.user.last_name +  " (" + self.user.username + ")"
        else:
            display_text = self.user.username
        return display_text

# class LocationIcon(models.Model):
#     icon_file = models.FileField(upload_to="img/")
#     icon_name = models.CharField(max_length=64, blank=True, null=True, default=u'')
#     def __unicode__(self):
#         return self.icon_name


class EventLocation(models.Model):
    #location_icon = models.ForeignKey(LocationIcon)
    icon_file = models.FileField(upload_to="img/")
    location_name = models.CharField(max_length=256, blank=True, null=True, default=u'')
    def __unicode__(self):
         return self.location_name


class CalendarEvent(models.Model):
    location = models.ForeignKey(EventLocation)
    event_title = models.CharField(max_length=64, blank=True, null=True, default=u'')
    event_subtitle = models.CharField(max_length=512, blank=True, null=True, default=u'')
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def pretty_time_format(self):
        verify_start = str(self.start_date.year) + "-" + str(self.start_date.month) + "-" + str(self.start_date.day)
        verify_end = str(self.end_date.year) + "-" + str(self.end_date.month) + "-" + str(self.end_date.day)
        if verify_start == verify_end:
            return custom_strftime('%B {S}', self.start_date) + " from " + self.start_date.strftime("%I:%M%p").lstrip("0") + " until " + self.end_date.strftime("%I:%M%p").lstrip("0")
        else:
            return custom_strftime('%B {S}', self.start_date) + " " + self.start_date.strftime("%I:%M%p").lstrip("0") + " until " + custom_strftime('%B {S}', self.end_date) + " " + self.end_date.strftime("%I:%M%p").lstrip("0")

    def __unicode__(self):
        return self.event_title + " | " + self.start_date.strftime("%A") + ", " + self.pretty_time_format()

    def iso_start_date(self):
        return self.start_date.isoformat('T')

    def iso_end_date(self):
        return self.end_date.isoformat('T')

class Announcement(models.Model):
    #crated_by = models.ForeignKey(User)
    created_by = models.ForeignKey(User, related_name='created_by')
    title = models.CharField(max_length=256, blank=False, null=False)
    content = models.TextField(blank=True, null=True, default="")
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.title + " | Owner: " + str(self.created_by.username) + " | " + self.content[:35]

    def iso_date(self):
        return  self.creation_date.isoformat('T')