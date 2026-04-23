from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Taskviewset


router = DefaultRouter()
router.register('tasks',Taskviewset,basename='tasks')

urlpatterns = [
    path('',include(router.urls)),
]