from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
]