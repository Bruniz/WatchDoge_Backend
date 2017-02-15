from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'watchdogesite.views.home', name='home'),
    url(r'^about/', 'watchdogesite.views.about', name='about'),
    url(r'^reviews/', 'watchdogesite.views.reviews', name='reviews'),
    url(r'^add_review', 'watchdogesite.views.add_review', name='add_review'),

#    url(r'^admin/', include(admin.site.urls)),
]


