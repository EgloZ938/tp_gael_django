from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Event, Participation

def event_list(request):
    """
    Affiche la liste de tous les événements
    Accessible par tous les utilisateurs (connectés ou non)
    """
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    """
    Affiche les détails d'un événement
    Permet aux utilisateurs connectés d'indiquer leur participation
    """
    event = get_object_or_404(Event, id=event_id)
    user_participating = False
    
    if request.user.is_authenticated:
        user_participating = Participation.objects.filter(user=request.user, event=event).exists()
        
        if request.method == 'POST':
            action = request.POST.get('action')
            
            if action == 'participate':
                # Ajouter l'utilisateur comme participant
                if not user_participating:
                    Participation.objects.create(user=request.user, event=event)
                    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
                    
            elif action == 'cancel':
                # Annuler la participation de l'utilisateur
                if user_participating:
                    Participation.objects.filter(user=request.user, event=event).delete()
                    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
    
    # Récupération du nombre de participants
    participant_count = event.get_participant_count()
    
    context = {
        'event': event,
        'participant_count': participant_count,
        'user_participating': user_participating,
    }
    
    return render(request, 'events/event_detail.html', context)

@login_required
def create_event(request):
    """
    Permet aux utilisateurs connectés de créer un nouvel événement
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        
        if title and description and date:
            event = Event.objects.create(
                title=title,
                description=description,
                date=date,
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('event_detail', args=[event.id]))
    
    return render(request, 'events/event_form.html')