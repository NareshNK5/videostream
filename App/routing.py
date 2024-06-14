# # from django.urls import re_path
# from django.urls import re_path as url, include 
# from . import consumers

# websocket_urlpatterns = [
#     url(r'ws/control/$', consumers.ControlConsumer.as_asgi()),
# ]

from django.urls import path
from .consumers import demo

websocket_urlpatterns = [
    path('ws/<str:command',demo.as_asgi()),
]