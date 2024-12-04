# communication/views.py  

from django.views.generic import TemplateView  
from rest_framework import generics  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response  
from rest_framework import status  
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate  
from .models import Message, Parent, Teacher  
from .serializers import MessageSerializer, ParentSerializer, TeacherSerializer, RegisterSerializer, LoginSerializer  
from django.conf import settings  
import os   

class FrontendView(TemplateView):  
    # Serve the main React application  
    template_name = os.path.join(settings.BASE_DIR, 'frontend', 'build', 'index.html')  

class MessageListCreateView(generics.ListCreateAPIView):  
    queryset = Message.objects.all()  
    serializer_class = MessageSerializer  
    permission_classes = [IsAuthenticated]  # Secured endpoint  

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Message.objects.all()  
    serializer_class = MessageSerializer  
    permission_classes = [IsAuthenticated]  # Secured endpoint  

class ParentListCreateView(generics.ListCreateAPIView):  
    queryset = Parent.objects.all()  
    serializer_class = ParentSerializer  
    permission_classes = [IsAuthenticated]  # Optional: Secure endpoint  

class TeacherListCreateView(generics.ListCreateAPIView):  
    queryset = Teacher.objects.all()  
    serializer_class = TeacherSerializer  
    permission_classes = [IsAuthenticated]  # Optional: Secure endpoint  

class RegisterView(generics.CreateAPIView):  
    serializer_class = RegisterSerializer  

    def perform_create(self, serializer):  
        # Here you might want to add logic for sending a welcome email or similar  
        user = serializer.save()  
        return Response({"message": "User created successfully", "username": user.username}, status=status.HTTP_201_CREATED)  

class LoginView(generics.GenericAPIView):  
    serializer_class = LoginSerializer  

    def post(self, request, *args, **kwargs):  
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)  

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])  
        if user is not None:  
            # Create a token or set user session if applicable  
            return Response({'message': 'Login successful', 'username': user.username}, status=status.HTTP_200_OK)  
        else:  
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)