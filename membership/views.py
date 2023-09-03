from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def membershipIndex(request):
    return render(request, 'membership.html')