from django.conf.urls import patterns, include, url
from django.contrib import admin

from codekeeper.views.home import HomePageView
from codekeeper.views.snippet import SnippetList, SnippetDetail
from codekeeper.views.person import PersonList, PersonDetail
from codekeeper.views.tag import TagList, TagDetail
from codekeeper.views.language import LanguageList, LanguageDetail
from codekeeper.views.search import SearchView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codekeeper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^snippets/$', SnippetList.as_view(), name="snippet-list"),
    url(r'^snippet/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name="snippet-detail"),
    url(r'^people/$', PersonList.as_view(), name="person-list"),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),
    url(r'^tags/$', TagList.as_view(), name="tag-list"),
    url(r'^tag/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name="tag-detail"),
    url(r'^languages/$', LanguageList.as_view(), name="language-list"),
    url(r'^language/(?P<pk>[0-9]+)/$', LanguageDetail.as_view(), name="language-detail"),
    url(r'^search/$', SearchView.as_view(), name="search-view"),
    url(r'^admin/', include(admin.site.urls)),
)
