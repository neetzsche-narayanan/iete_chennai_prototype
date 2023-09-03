"""
URL configuration for iete_chennai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('membership/', include(('membership.urls', 'membership'), namespace='membership')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('committee/', include(('executive_committee.urls', 'committee'), namespace='committee')),
    path('newsletter/', include(('newsletter.urls', 'newsletter'), namespace='newsletter')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
