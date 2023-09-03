from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactIndex, name="contactIndex"),
]