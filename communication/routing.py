from django.urls import re_path  
from . import consumers  

websocket_urlpatterns = [  
    re_path(r'ws/send-messages/$', consumers.MessageConsumer.as_asgi()),  # Updated path  
    re_path(r'ws/parents/$', consumers.ParentConsumer.as_asgi()),  
    re_path(r'ws/teachers/$', consumers.TeacherConsumer.as_asgi()),  
]