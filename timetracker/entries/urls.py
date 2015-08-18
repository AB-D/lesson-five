from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from . import views


urlpatterns = [
	url(r'^$', RedirectView.as_view(url = reverse_lazy('client-list')), name= 'home'),
   	url(r'^clients/$', views.ClientCreateView.as_view(), name='client-list'),
    url(r'^clients/(?P<pk>\d+)/$', views.ClientUpdateView.as_view(), name='client-detail'),
    url(r'^entries/$', views.EntryCreateView.as_view(), name='entry-list'),
    url(r'^projects/$', views.ProjectCreateView.as_view(), name='project-list'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name='project-detail'),
]


