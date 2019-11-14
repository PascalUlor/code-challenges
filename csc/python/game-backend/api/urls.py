from django.urls import include, path
from django.conf.urls import url
from . import api

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]
