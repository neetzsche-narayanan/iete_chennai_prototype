from django.urls import path
from . import views

urlpatterns = [
    path('',views.EventListView.as_view(),name="eventList"),
    path('<slug:slug>/', views.EventDetailView.as_view(),name="eventDetail"),
    path('2022/CHENCON/', views.chenCon22,name="chencon22"),
]