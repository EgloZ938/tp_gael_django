from django.contrib import admin
from .models import Event, Participation

class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_by', 'get_participant_count')
    list_filter = ('date', 'created_by')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    inlines = [ParticipationInline]

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('user__username', 'event__title')