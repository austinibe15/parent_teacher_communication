# communication/urls.py  

from django.urls import path  
from .views import (  
    FrontendView,  
    MessageListCreateView,  
    MessageDetailView,  
    ParentListCreateView,  
    TeacherListCreateView,  
    RegisterView,  
    LoginView,  
)  

urlpatterns = [  
    # Serve the React frontend  
    path('', FrontendView.as_view(), name='frontend'),  
    # API endpoints for messages management  
    path('api/messages/', MessageListCreateView.as_view(), name='message-list-create'),  
    path('api/messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),  
    # API endpoints for parent and teacher management  
    path('api/parents/', ParentListCreateView.as_view(), name='parent-list-create'),  
    path('api/teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),  
    # User authentication endpoints  
    path('api/register/', RegisterView.as_view(), name='register'),  
    path('api/login/', LoginView.as_view(), name='login'),  
]