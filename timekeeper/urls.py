from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from timekeeper.views.activity import ActivityList, ActivityDetail
from timekeeper.views.place import PlaceList, PlaceDetail
from timekeeper.views.person import PersonList, PersonDetail
from timekeeper.views.search import SearchView

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('timekeeper.views.main',
        url(r'^$', 'home'),
        url(r'^browse/$', 'api_root'),

        url(r'^activities/$', ActivityList.as_view(), name="activity-list"),
        url(r'^activity/(?P<pk>[0-9]+)/$', ActivityDetail.as_view(), name="activity-detail"),
        url(r'^places/$', PlaceList.as_view(), name="place-list"),
        url(r'^place/(?P<pk>[0-9]+)/$', PlaceDetail.as_view(), name="place-detail"),
        url(r'^people/$', PersonList.as_view(), name="person-list"),
        url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),
        url(r'^search/$', SearchView.as_view(), name="search-view"),

        url(r'^admin/', include(admin.site.urls)),
))
