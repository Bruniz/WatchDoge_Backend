from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'watchdogesite.views.home', name='home'),
    url(r'^about/', 'watchdogesite.views.about', name='about'),
    url(r'^reports/add', 'watchdogesite.views.add_report', name='add_report'),
    url(r'^reports/', 'watchdogesite.views.reports', name='reports'),
    url(r'^api/report/add', 'watchdogeapi.views.add', name='api_add_report'),


#    url(r'^admin/', include(admin.site.urls)),
]


