from django.db import models
from time import timezone
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=500)
    event_image = models.ImageField("Image")
    creation_date = models.DateField("Date Published")
    event_text = models.TextField("Event Text")
    event_date = models.DateTimeField("Event Date")
    button_url = models.URLField("Button URL")
    button_text = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f"{self.creation_date}: {self.event_name}"
    
    def get_absolute_url(self):
        return reverse('events:eventDetail',args=[str(self.slug)])