from django.urls import path
from socialmedia import views

urlpatterns = [
    # About ME
    path('all/', views.SocialMediasApi.as_view(), name="Social Media")
]
