"""suzatadjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from aboutme.urls import urlpatterns as aboutMeUrl
from projects.urls import urlpatterns as projectsUrl
from services.urls import urlpatterns as servicesUrl
from socialmedia.urls import urlpatterns as socialmediaUrl
from getintouch.urls import urlpatterns as messageUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/aboutme/', include(aboutMeUrl)),
    path('api/projects/', include(projectsUrl)),
    path('api/services/', include(servicesUrl)),
    path('api/socialmedia/', include(socialmediaUrl)),
    path('api/message/', include(messageUrl)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
