"""
URL configuration for parent_teacher_communication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#parent_teacher communication/urls.py

from django.contrib import admin  
from django.urls import path, include  
from django.http import JsonResponse  
from django.views.generic import TemplateView  
from django.views.static import serve  
from django.conf import settings  
from django.conf.urls.static import static  
import os  

from communication.views import (  
    MessageListCreateView,  
    MessageDetailView,  
    ParentListCreateView,  
    TeacherListCreateView,  
    RegisterView,  
    LoginView,  
)  
from communication.routing import websocket_urlpatterns  

# API root view to list available endpoints  
def api_root(request):  
    return JsonResponse({  
        'messages': '/api/messages/',  
        'parents': '/api/parents/',  
        'teachers': '/api/teachers/',  
        'register': '/api/register/',  
        'login': '/api/login/',  
    })  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('api/', api_root, name='api-root'),  
    path('api/messages/', MessageListCreateView.as_view(), name='message-list-create'),  
    path('api/messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),  
    path('api/parents/', ParentListCreateView.as_view(), name='parent-list-create'),  
    path('api/teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),  
    path('api/register/', RegisterView.as_view(), name='register'),  
    path('api/login/', LoginView.as_view(), name='login'),  
    path('ws/', include(websocket_urlpatterns)),  # WebSocket URLs  

    # Serve the main React app  
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Serve root index.html  
    # Serve static files from the React build  
    path('static/<path:path>/', serve, {'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'build', 'static')}),  
]  

# Serve static files in development mode  
if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)