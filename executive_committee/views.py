from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def committeeIndex(request):
    return render(request, 'executive_committee.html')