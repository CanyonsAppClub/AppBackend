from django.forms.extras.widgets import SelectDateWidget
from django.db import models
#from django.forms import forms, DateField
from django.contrib.auth.models import User

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


class AppUser(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)

class LocationIcon(models.Model):
    icon_file = models.FileField(upload_to="img/")
    icon_name = models.CharField(max_length=64, blank=True, null=True, default=u'')
    def __unicode__(self):
        return self.icon_name

class EventLocation(models.Model):
    location_icon = models.ForeignKey(LocationIcon)
    location_name = models.CharField(max_length=256, blank=True, null=True, default=u'')
    def __unicode__(self):
         return self.location_name


class CalendarEvent(models.Model):
    location = models.ForeignKey(EventLocation)
    event_title = models.CharField(max_length=64, blank=True, null=True, default=u'')
    event_subtitle = models.CharField(max_length=512, blank=True, null=True, default=u'')
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    def __unicode__(self):
        return self.event_title + " | " + str(self.start_date.date())
