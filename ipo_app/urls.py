from django.urls import path
from . import views

urlpatterns = [
    path('ipos/', views.ipo_list), 
    path('ipos/<int:pk>/', views.ipo_detail), 
    path('test/', views.test_api),  
]
