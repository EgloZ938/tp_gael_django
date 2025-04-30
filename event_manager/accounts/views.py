from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse

def login_view(request):
    """
    Gère la connexion des utilisateurs
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger vers la liste des événements après connexion
                return redirect('event_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """
    Gère la déconnexion des utilisateurs
    """
    logout(request)
    return redirect('login')

def register_view(request):
    """
    Gère l'inscription des nouveaux utilisateurs
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})