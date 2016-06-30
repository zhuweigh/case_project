from django.conf.urls import patterns, include, url
from django.contrib import admin 
from case import views 
from django.utils.translation import gettext_lazy as _
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'e_case.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
       # url(r'^admin/', include(admin.site.urls)),
        url(_(r'^list/') ,views.CaseList,name='case_list'),
        url(_(r'^detail/(?P<case_id>\d+)/') ,views.CaseDetail,name='case_detail'),
	url(_(r'^search/$'), views.case_search, name='case_searchs'),
	#url(r'^pdf/$',views.export_pdf,name='pdf_show'),
	#url(r'^pdf/$', views.HelloPDFView.as_view()),
	#url(r'^pdf/$', views.generate_pdf_view),
	url(_(r'^pdf/(?P<case_id>\d+)$'), views.test_pdf,name='show_pdf'),
)
                                                            
