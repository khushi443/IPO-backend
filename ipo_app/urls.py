# ipo_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('ipos/', views.IPOListCreateView.as_view(), name='ipo-list'),
    path('ipos/<int:pk>/', views.ipo_detail),  # keep if you have detail view
    path('test/', views.test_api),             # optional
]
