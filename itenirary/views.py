# django modules
from django.views.generic import DetailView, ListView
from django.http import Http404
# models
from .models import Event, Day

class DayListView(ListView):
    model = Day
    template_name = "itenirary/day_listed.html"
    context_object_name = "days"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = context[
            self.context_object_name].filter(release=True).order_by('number')
        return context

class DayDetailView(DetailView):
    model = Day
    template_name = "itenirary/day_detail.html"
    context_object_name = "day_details"
    slug_url_kwarg = 'number'
    slug_field = 'number'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add a context of a list of events for the current day
        context['event_list'] = Event.objects.filter(
            day=context[self.context_object_name].pk).order_by('time')
        # Add a context of a list of days that are viewable
        context['days'] = Day.objects.filter(release=True).order_by('number')
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = "itenirary/event_detail.html"
    context_object_name = "event_details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context[self.context_object_name].day.release:
            return context
        else:
            raise Http404