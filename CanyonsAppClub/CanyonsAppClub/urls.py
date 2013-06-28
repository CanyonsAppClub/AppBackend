from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'AppBackend.views.home', name='home'),
    # url(r'^CanyonsAppClub/', include('CanyonsAppClub.foo.urls')),

    url(r'^count', 'AppBackend.views.count', name='count'),

    #url(r'^manage/icons/', 'AppBackend.views.list_files', name='list'),
    url(r'^manage/icons/', 'AppBackend.views.list_files', name='listfiles'),

    url(r'^loctest', 'AppBackend.views.loc_test', name="loc_test"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'app/events/', 'AppBackend.views.app_calendar_list', name='app_calendar_list'),

    url(r'^debug', 'AppBackend.views.debug_view'),

    url(r'app/loc_icon_ref/', 'AppBackend.views.app_location_icon', name='app_location_icon'),

    url(r'app/json/events/', 'AppBackend.views.app_json_event_list'),
    url(r'app/json/locations/', 'AppBackend.views.app_json_location_list'),
    url(r'app/json/icons/', 'AppBackend.views.app_json_icon_list'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)