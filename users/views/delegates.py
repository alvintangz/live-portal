from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from users.models import Delegate
from django.shortcuts import redirect
import urllib
from users.auth.mixins import PartnerRequiredMixin
from users.constants.seeking_statuses import SEEKING_STATUSES
from users.constants.universities import COMMON_UNIVERSITIES
from users.constants.student_types import STUDENT_TYPES

class DelegatesListView(PartnerRequiredMixin, ListView):
    model = Delegate
    template_name = "users/delegate/listed.html"
    context_object_name = "delegates"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Pass filters
        context["filters"] = dict()
        context["filters"]["seeking_statuses"] = SEEKING_STATUSES
        context["filters"]["universities"] = COMMON_UNIVERSITIES
        context["filters"]["student_types"] = STUDENT_TYPES
        # Get filters
        ss_filter = self.request.GET.get('ss','')
        un_filter = self.request.GET.get('un','')
        st_filter = self.request.GET.get('st','')
        # Pass get filter values and actually filter
        context["filters"]["default"] = dict()
        if ss_filter != "":
            context["filters"]["default"]["seeking_statuses"] = ss_filter
            context[self.context_object_name] = context[
                self.context_object_name].filter(
                    seeking_status=urllib.parse.unquote(ss_filter))
        if un_filter != "":
            context["filters"]["default"]["universities"] = un_filter
            context[self.context_object_name] = context[
                self.context_object_name].filter(
                    school=urllib.parse.unquote(un_filter))
        if st_filter != "":
            context["filters"]["default"]["student_types"] = st_filter
            context[self.context_object_name] = context[
                self.context_object_name].filter(
                    year_of_study=(urllib.parse.unquote(st_filter)))
            print(urllib.parse.unquote(un_filter))
        # If no filters
        if ss_filter == "" and un_filter == "" and st_filter == "":
            context["filters"]["none"] = True
        return context

    def get_queryset(self):
        original = super().get_queryset()
        return original.filter(is_invisible=False).order_by("user__first_name")

class DelegatesDetailView(PartnerRequiredMixin, DetailView):
    model = Delegate
    template_name = "users/delegate/detail.html"
    context_object_name = "delegate"