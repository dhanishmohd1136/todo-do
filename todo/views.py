from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Task
from .serializers import TaskSerilizer

# Create your views here.

class Taskviewset(viewsets.ModelViewSet):

    serializer_class=TaskSerilizer
    permission_classes =[permissions.IsAuthenticated]


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)