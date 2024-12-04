"""
ASGI config for parent_teacher_communication project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  
from django.core.asgi import get_asgi_application  
from channels.routing import ProtocolTypeRouter, URLRouter  
from channels.auth import AuthMiddlewareStack  
from communication import routing  # Import your routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parent_teacher_communication.settings')  

application = ProtocolTypeRouter({  
    "http": get_asgi_application(),  
    # Define WebSocket handlers here  
    "websocket": AuthMiddlewareStack(  
        URLRouter(  
            routing.websocket_urlpatterns  # Add your WebSocket URL patterns  
        )  
    ),  
})