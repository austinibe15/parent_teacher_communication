# communication/serializers.py  

from rest_framework import serializers  
from django.contrib.auth.models import User  
from .models import Message, Parent, Teacher  

class MessageSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Message  
        fields = ('id', 'sender', 'receiver', 'content', 'timestamp', 'is_read', 'subject')  # Include all necessary fields  

class ParentSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Parent  
        fields = ('user', 'phone_number')  # Ensure phone_number field is included  

class TeacherSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Teacher  
        fields = ('user', 'subject')  # Ensure subject field is included  

class RegisterSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ('username', 'password')  
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only  

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  # Hash the password  
        user.save()  
        return user  

class LoginSerializer(serializers.Serializer):  
    username = serializers.CharField()  
    password = serializers.CharField(write_only=True)  # Password should be write-only  

    def validate(self, attrs):  
        username = attrs.get('username')  
        password = attrs.get('password')  

        if not User.objects.filter(username=username).exists():  
            raise serializers.ValidationError("User does not exist.")  

        return attrs