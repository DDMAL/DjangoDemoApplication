from django.conf.urls import patterns, include, url
from django.contrib import admin

from codekeeper.views.home import HomePageView
from codekeeper.views.snippet import SnippetList, SnippetDetail
from codekeeper.views.person import PersonList, PersonDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codekeeper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^snippets/$', SnippetList.as_view(), name="snippet-list"),
    url(r'^snippet/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name="snippet-detail"),
    url(r'^people/$', PersonList.as_view(), name="person-list"),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),
    url(r'^admin/', include(admin.site.urls)),
)
