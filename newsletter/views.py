from django.shortcuts import render

# Create your views here.
def newsletterIndex(request):
    return render(request, 'newsletter.html')