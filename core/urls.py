from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:pk>/', views.event_detail, name='event-detail')
]