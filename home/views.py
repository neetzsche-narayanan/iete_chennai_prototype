from django.shortcuts import render
from events.models import Event
import datetime
from zoneinfo import ZoneInfo

# Create your views here.
def homeIndex(request):
    current_time = datetime.datetime.now(ZoneInfo('Asia/Kolkata'))
    event_list= Event.objects.filter(event_date__gte=current_time)
    return render(request, 'home.html',{'event_list':event_list,})