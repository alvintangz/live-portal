# django modules
from django.views.generic import DetailView, ListView
from django.http import Http404
# models
from .models import Event, Day
# helpers
from users.auth.mixins import TypesRequiredMixin
from portal.functions import hashid_decode

class DayListView(TypesRequiredMixin, ListView):
    model = Day
    template_name = "itenirary/day_listed.html"
    context_object_name = "days"
    delegate_allowed = True
    partner_allowed = True
    judge_allowed = True

    def get_queryset(self):
        original = super().get_queryset()
        return original.filter(release=True).order_by('number')

class DayDetailView(TypesRequiredMixin, DetailView):
    model = Day
    template_name = "itenirary/day_detail.html"
    context_object_name = "day_details"
    slug_url_kwarg = 'number'
    slug_field = 'number'
    delegate_allowed = True
    partner_allowed = True
    judge_allowed = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a context of a list of events for the current day
        context['event_list'] = Event.objects.filter(
            day=context[self.context_object_name].pk).order_by('time')
        # Add a context of a list of days that are viewable
        context['days'] = Day.objects.filter(release=True).order_by('number')
        return context

class EventDetailView(TypesRequiredMixin, DetailView):
    model = Event
    template_name = "itenirary/event_detail.html"
    context_object_name = "event_details"
    delegate_allowed = True
    partner_allowed = True
    judge_allowed = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context[self.context_object_name].day.release:
            return context
        else:
            raise Http404