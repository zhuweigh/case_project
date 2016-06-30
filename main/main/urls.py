from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
#from deatil.views imp
urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'e_case.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
   	url(_(r'^case/') ,include('case.urls',namespace='case')),
	url(_(r'^rosetta/'), include('rosetta.urls')),
)
