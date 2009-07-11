from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^$', 'profile.views.main'),
     (r'^home', 'profile.views.home'),
     (r'^tabbedjs', 'profile.views.tabbedjs'),
     (r'^style', 'profile.views.style'),
)

