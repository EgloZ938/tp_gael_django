from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # GET /events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # GET /events/id_event
    path('create/', views.create_event, name='create_event'),  # Pour créer un événement
]
