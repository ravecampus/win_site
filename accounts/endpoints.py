from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .api import *


urlpatterns = [
    url(r'^account/$', AccountAPI.as_view({'get':'list','post':'create'}), name="user_"),
    url(r'^account/(?P<user_id>[0-9]+)/$', AccountAPI2.as_view({
        'get':'get',
        'put':'update',
        'delete':'delete'
        ,}), name="users_"),
]
urlpatterns = format_suffix_patterns(urlpatterns)