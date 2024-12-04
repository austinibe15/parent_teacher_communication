# communication/models.py  
from django.db import models  
from django.contrib.auth.models import User  

class Message(models.Model):  
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')  
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')  
    content = models.TextField()  
    timestamp = models.DateTimeField(auto_now_add=True)  
    is_read = models.BooleanField(default=False)  
    subject = models.CharField(max_length=255, blank=True, null=True)  

    class Meta:  
        ordering = ['-timestamp']  
        verbose_name = 'Message'  
        verbose_name_plural = 'Messages'  

    def __str__(self):  
        return f'Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}'  

class Parent(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number field  

    def __str__(self):  
        return f'Parent: {self.user.username}'  

class Teacher(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    subject = models.CharField(max_length=100, blank=True, null=True)  # Subject field  

    def __str__(self):  
        return f'Teacher: {self.user.username}'