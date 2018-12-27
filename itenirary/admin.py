from django.contrib import admin
from .models import Day, Event

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_formatted_time', 'day',)
    order_by = ('day',)
    list_filter = ('day', 'venue_name',)