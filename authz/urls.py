from django.urls import path
from authz.views import *


urlpatterns =[
    path("", signup, name='signup'),
    path("", login, name='login'),
    path("", logout, name='logout'),
]