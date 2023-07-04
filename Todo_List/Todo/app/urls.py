
from django.urls import path,include
from .views import main,tasks
urlpatterns = [
    
    path('',main,name='main'),
    path('tasks/',tasks,name='tasks'),
]