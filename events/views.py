from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .models import Event
from django import forms
from zoneinfo import ZoneInfo
import datetime

class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_objects'
    template_name = 'events.html'
    paginate_by = 9

    def get_queryset(self) -> QuerySet[Any]:
        return Event.objects.order_by("-creation_date")

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'indiv_event.html'
    context_object_name = 'event_post'

def chenCon22(request):
    return render(request,'special_templates/chencon22.html')