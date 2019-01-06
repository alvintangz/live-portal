from django.contrib import admin
from rounds.models.presentationvideos import PresentationVideo

@admin.register(PresentationVideo)
class PresentationVideoAdmin(admin.ModelAdmin):
    list_display = ('team', 'round',)
    list_filter = ('team', 'round',)
    ordering = ('team', 'round',)
    exclude = ('slug',)