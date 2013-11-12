from django.contrib import admin
from AppBackend.models import AppUser
from AppBackend.models import CalendarEvent
from AppBackend.models import EventLocation
from AppBackend.models import Announcement
#from AppBackend.models import LocationIcon
from django import forms
from django.db import models
import json

# class CalendarEventAdmin(admin.ModelAdmin):
#     class Meta:
#         model = CalendarEvent
#         cleaned = ""
#         for cleaned in model.objects.all():
#                 cleaned = json.JSONEncoder().encode(cleaned)
#         def clean_name(self):
#             return self.cleaned

#     exclude = ['title']
#     form = CalendarEvent

# class EventLocationAdmin(admin.ModelAdmin):
#     list_display = ('locationName')

# class EventLocationForm(forms.ModelForm):
#     location_name = forms.CharField()
#     class Meta:
#         model = CalendarEvent
#
# class EventLocationAdmin(admin.ModelAdmin):
#     form = EventLocationForm

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

#admin.site.register(AppUser)
admin.site.register(CalendarEvent)
admin.site.register(EventLocation)
admin.site.register(Announcement, ArticleAdmin)
#admin.site.register(LocationIcon)