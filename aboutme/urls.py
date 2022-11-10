

from django.urls import path
from aboutme import views


urlpatterns = [
    # About ME
    path('detail/', views.AboutMeApi.as_view(), name="About Me"),
    path('greeting/', views.GreetingApi.as_view(), name="Greeting")
]
