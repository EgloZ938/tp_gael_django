"""
URL configuration for event_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Page d'accueil = page de connexion
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
]

# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # GET /events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # GET /events/id_event
    path('create/', views.create_event, name='create_event'),  # Pour créer un événement (optionnel)
]