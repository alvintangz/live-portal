from django.contrib import admin
from .models import Day, Event

class EventInline(admin.StackedInline):
    model = Event
    extra = 0

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    inlines = (EventInline,)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_formatted_time', 'day',)
    order_by = ('day',)
    list_filter = ('day', 'venue_name',)