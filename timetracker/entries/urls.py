from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^clients/$', views.ClientCreateView.as_view(), name='client-list'),
    url(r'^clients/(?P<pk>\d+)/$', views.ClientUpdateView.as_view(), name='client-detail'),
    url(r'^entries/$', views.entries, name='entry-list'),
    url(r'^projects/$', views.ProjectCreateView.as_view(), name='project-list'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name='project-detail'),
]
